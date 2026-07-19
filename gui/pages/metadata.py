import os
import customtkinter as ctk

from tkinter import filedialog
from tkinter import messagebox

from services.metadata.metadata_service import MetadataService

from services.export.json_export import JsonExporter
from services.export.csv_export import CsvExporter
from services.export.pdf_export import PdfExporter

from gui.styles.colors import Colors

from gui.components.image_preview import ImagePreview
from gui.components.metadata_table import MetadataTable
from gui.components.hash_card import HashCard
from gui.components.risk_card import RiskCard
from gui.components.security_card import SecurityCard
from gui.components.status_bar import StatusBar
from gui.components.progress_card import ProgressCard

from core.metadata.sanitizer import MetadataSanitizer


class MetadataPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=Colors.BACKGROUND
        )
        
        self.file_path = None
        self.analysis_result = None

        self.build_toolbar()

        self.build_body()

        self.build_statusbar()

    #########################################################

    def build_toolbar(self):

        self.toolbar = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.toolbar.pack(
            fill="x",
            padx=20,
            pady=(15, 5)
        )

        self.select_btn = ctk.CTkButton(
            self.toolbar,
            text="📂 Select Image",
            width=150,
            command=self.select_image
        )

        self.select_btn.pack(
            side="left",
            padx=5
        )

        self.analyze_btn = ctk.CTkButton(
            self.toolbar,
            text="🧪 Analyze",
            width=120,
            command=self.analyze
        )

        self.analyze_btn.pack(
            side="left",
            padx=5
        )

        self.json_btn = ctk.CTkButton(
            self.toolbar,
            text="📄 JSON",
            width=110,
            state="disabled",
            command=self.export_json
        )

        self.json_btn.pack(
            side="left",
            padx=5
        )

        self.csv_btn = ctk.CTkButton(
            self.toolbar,
            text="📊 CSV",
            width=110,
            state="disabled",
            command=self.export_csv
        )

        self.csv_btn.pack(
            side="left",
            padx=5
        )

        self.pdf_btn = ctk.CTkButton(
            self.toolbar,
            text="📑 PDF",
            width=110,
            state="disabled",
            command=self.export_pdf
        )

        self.pdf_btn.pack(
            side="left",
            padx=5
        )

        self.clean_btn = ctk.CTkButton (
            self.toolbar,
            text="🧹 Remove Metadata",
            width=170,
            state="disabled",
            command=self.remove_metadata
        )

        self.clean_btn.pack(
            side="left",
            padx=5
        )

        self.filename = ctk.CTkLabel(
            self,
            text="No image selected",
            anchor="w",
            text_color=Colors.SUBTEXT
        )

        self.filename.pack(
            fill="x",
            padx=25,
            pady=(0, 10)
        )

        self.folder_btn = ctk.CTkButton(
            self.toolbar,
            text="📂 Open Exports",
            width=150,
            command=self.open_export_folder
        )

        self.folder_btn.pack(
            side="left",
            padx=5
        )

    #########################################################

    def build_body(self):

        self.body = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.body.pack(
            fill="both",
            expand=True,
            padx=10
        )

        #####################################################

        self.left = ctk.CTkFrame(
            self.body,
            width=360,
            fg_color="transparent"
        )

        self.left.pack(
            side="left",
            fill="y",
            padx=(10,5)
        )

        #####################################################

        self.right = ctk.CTkFrame(
            self.body,
            fg_color="transparent"
        )

        self.right.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(5,10)
        )

        #####################################################

        self.preview = ImagePreview(
            self.left
        )

        self.preview.pack(
            fill="x",
            pady=10
        )

        #####################################################

        self.security = SecurityCard(
            self.left
        )

        self.security.pack(
            fill="x",
            pady=10
        )

        #####################################################

        self.progress = ProgressCard(
            self.left
        )

        self.progress.pack(
            fill="x",
            pady=10
        )

        #####################################################

        self.risk_frame = ctk.CTkFrame(
            self.left,
            fg_color="transparent"
        )

        self.risk_frame.pack(
            fill="x",
            pady=10
        )

        #####################################################

        self.table = MetadataTable(
            self.right
        )

        self.table.pack(
            fill="both",
            expand=True
        )

        #####################################################

        self.hash_frame = ctk.CTkFrame(
            self.right,
            fg_color="transparent"
        )

        self.hash_frame.pack(
            fill="x",
            pady=15
        )

    #########################################################

    def build_statusbar(self):

        self.status = StatusBar(
            self
        )

        self.status.pack(
            side="bottom",
            fill="x"
        )
    
    #########################################################
    # Select Image
    #########################################################

    def select_image(self):

        path = filedialog.askopenfilename(

            title="Select Image",

            filetypes=[

                ("Image Files",
                 "*.jpg *.jpeg *.png *.bmp *.gif *.webp *.tiff")

            ]

        )

        if not path:
            return

        self.file_path = path

        self.filename.configure(
            text=f"Selected : {os.path.basename(path)}"
        )

        self.preview.load_image(path)

        self.status.set_status(
            "Image Loaded Successfully"
        )

        self.progress.update_progress(
            0.10
        )

    #########################################################
    # Analyze Image
    #########################################################

    def analyze(self):

        if not self.file_path:

            messagebox.showwarning(

                "No Image",

                "Please select an image first."

            )

            return

        try:

            self.status.set_status(
                "Analyzing Image..."
            )

            self.progress.update_progress(
                0.25
            )

            self.analysis_result = MetadataService.analyze(

                self.file_path

            )

            self.progress.update_progress(
                0.50
            )

            #################################################

            self.table.load(

                self.analysis_result

            )

            #################################################

            for widget in self.hash_frame.winfo_children():

                widget.destroy()

            #################################################

            hashes = self.analysis_result["hashes"]

            HashCard(

                self.hash_frame,

                "MD5",

                hashes["md5"]

            ).pack(

                fill="x",

                pady=5

            )

            HashCard(

                self.hash_frame,

                "SHA-256",

                hashes["sha256"]

            ).pack(

                fill="x",

                pady=5

            )

            HashCard(

                self.hash_frame,

                "SHA-512",

                hashes["sha512"]

            ).pack(

                fill="x",

                pady=5

            )

            #################################################

            for widget in self.risk_frame.winfo_children():

                widget.destroy()

            RiskCard(

                self.risk_frame,

                self.analysis_result["risk"]

            ).pack(

                fill="x",

                pady=10

            )

            #################################################
            # Security Score
            #################################################

            risk = self.analysis_result["risk"]["Risk Score"]

            score = max(

                100 - risk,

                0

            )

            self.security.update_score(

                score

            )

            #################################################

            self.progress.update_progress(

                1.0

            )

            #################################################

            self.json_btn.configure(

                state="normal"

            )

            self.csv_btn.configure(

                state="normal"

            )

            self.pdf_btn.configure(

                state="normal"

            )

            self.clean_btn.configure(

                state="normal"

            )

            #################################################

            self.status.set_status(

                "Analysis Completed"

            )

        except Exception as error:

            messagebox.showerror(

                "Analysis Failed",

                str(error)

            )

            self.status.set_status(

                "Analysis Failed"

            )

        #########################################################
    # Export JSON
    #########################################################

    def export_json(self):

        if not self.analysis_result:

            messagebox.showwarning(
                "No Analysis",
                "Please analyze an image first."
            )

            return

        try:

            output = JsonExporter.export(
                self.analysis_result,
                "exports/report.json"
            )

            self.status.set_status(
                "JSON Report Exported"
            )

            messagebox.showinfo(
                "Success",
                f"JSON exported successfully.\n\n{output}"
            )

        except Exception as error:

            messagebox.showerror(
                "Export Failed",
                str(error)
            )

    #########################################################
    # Export CSV
    #########################################################

    def export_csv(self):

        if not self.analysis_result:

            messagebox.showwarning(
                "No Analysis",
                "Please analyze an image first."
            )

            return

        try:

            output = CsvExporter.export(
                self.analysis_result,
                "exports/report.csv"
            )

            self.status.set_status(
                "CSV Report Exported"
            )

            messagebox.showinfo(
                "Success",
                f"CSV exported successfully.\n\n{output}"
            )

        except Exception as error:

            messagebox.showerror(
                "Export Failed",
                str(error)
            )

    #########################################################
    # Export PDF
    #########################################################

    def export_pdf(self):

        if not self.analysis_result:

            messagebox.showwarning(
                "No Analysis",
                "Please analyze an image first."
            )

            return

        try:

            output = PdfExporter.export(
                self.analysis_result,
                "exports/report.pdf"
            )

            self.status.set_status(
                "PDF Report Exported"
            )

            messagebox.showinfo(
                "Success",
                f"PDF exported successfully.\n\n{output}"
            )

        except Exception as error:

            messagebox.showerror(
                "Export Failed",
                str(error)
            )

    #########################################################
    # Open Export Folder
    #########################################################

    def open_export_folder(self):

        folder = os.path.abspath("exports")

        os.makedirs(
            folder,
            exist_ok=True
        )

        os.startfile(folder)

    #########################################################
    # Remove Metadata
    #########################################################

    def remove_metadata(self):

        messagebox.showinfo(

            "Coming Soon",

            "Metadata Sanitizer will be implemented in Sprint 7."

        )
