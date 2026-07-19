import customtkinter as ctk
from tkinter import filedialog, messagebox
import os

from utils.theme import Theme
from services.crypto.encryption_service import EncryptionService


class EncryptPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent, fg_color=Theme.BG)

        self.selected_file = ""

        title = ctk.CTkLabel(
            self,
            text="🔐 Encrypt Image",
            font=("Segoe UI", 28, "bold"),
            text_color=Theme.PRIMARY
        )
        title.pack(pady=(20, 10))

        self.file_label = ctk.CTkLabel(
            self,
            text="No file selected",
            font=("Segoe UI", 14)
        )
        self.file_label.pack(pady=10)

        ctk.CTkButton(
            self,
            text="📂 Select Image",
            width=220,
            command=self.select_file
        ).pack(pady=10)

        self.password = ctk.CTkEntry(
            self,
            width=320,
            placeholder_text="Enter Password",
            show="*"
        )
        self.password.pack(pady=10)

        self.progress = ctk.CTkProgressBar(
            self,
            width=500
        )
        self.progress.pack(pady=20)
        self.progress.set(0)

        self.status = ctk.CTkLabel(
            self,
            text="Waiting...",
            font=("Segoe UI", 14)
        )
        self.status.pack()

        ctk.CTkButton(
            self,
            text="🔒 Encrypt",
            width=220,
            fg_color=Theme.PRIMARY,
            text_color="black",
            command=self.encrypt
        ).pack(pady=20)

    def select_file(self):

        filename = filedialog.askopenfilename(

            title="Select Image",

            filetypes=[

                (
                    "Images",
                    "*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.webp"
                )

            ]

        )

        if filename:

            self.selected_file = filename

            self.file_label.configure(
                text=os.path.basename(filename)
            )

    def encrypt(self):

        if not self.selected_file:

            messagebox.showerror(
                "Error",
                "Please select an image."
            )

            return

        password = self.password.get()

        if len(password) < 8:

            messagebox.showerror(
                "Error",
                "Password must be at least 8 characters."
            )

            return

        self.progress.set(0.2)

        output = filedialog.asksaveasfilename(

            defaultextension=".enc",

            filetypes=[("Encrypted File", "*.enc")]

        )

        if not output:

            return

        try:

            self.progress.set(0.5)

            EncryptionService.encrypt(
                self.selected_file,
                output,
                password
            )

            self.progress.set(1)

            self.status.configure(
                text="Encryption Completed Successfully"
            )

            messagebox.showinfo(
                "Success",
                "Image encrypted successfully."
            )

        except Exception as e:

            self.progress.set(0)

            messagebox.showerror(
                "Error",
                str(e)
            )