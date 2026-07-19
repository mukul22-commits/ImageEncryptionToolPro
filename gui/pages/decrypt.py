import customtkinter as ctk
from tkinter import filedialog, messagebox
import os

from utils.theme import Theme
from services.crypto.encryption_service import EncryptionService


class DecryptPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent, fg_color=Theme.BG)

        self.selected_file = ""

        ctk.CTkLabel(
            self,
            text="🔓 Decrypt Image",
            font=("Segoe UI", 28, "bold"),
            text_color=Theme.PRIMARY
        ).pack(pady=(20, 10))

        self.file_label = ctk.CTkLabel(
            self,
            text="No encrypted file selected"
        )

        self.file_label.pack(pady=10)

        ctk.CTkButton(
            self,
            text="Select Encrypted File",
            command=self.select_file,
            width=220
        ).pack(pady=10)

        self.password = ctk.CTkEntry(
            self,
            placeholder_text="Enter Password",
            show="*",
            width=320
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
            text="Waiting..."
        )

        self.status.pack()

        ctk.CTkButton(
            self,
            text="Decrypt",
            width=220,
            fg_color=Theme.PRIMARY,
            text_color="black",
            command=self.decrypt
        ).pack(pady=20)

    def select_file(self):

        filename = filedialog.askopenfilename(
            title="Select Encrypted File",
            filetypes=[("Encrypted Files", "*.enc")]
        )

        if filename:
            self.selected_file = filename
            self.file_label.configure(
                text=os.path.basename(filename)
            )

    def decrypt(self):

        if not self.selected_file:
            messagebox.showerror(
                "Error",
                "Please select an encrypted file."
            )
            return

        password = self.password.get()

        if len(password) < 8:
            messagebox.showerror(
                "Error",
                "Password must contain at least 8 characters."
            )
            return

        output = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[
                ("JPEG Image", "*.jpg"),
                ("PNG Image", "*.png"),
                ("All Files", "*.*")
            ]
        )

        if not output:
            return

        try:

            self.progress.set(0.5)

            EncryptionService.decrypt(
                self.selected_file,
                output,
                password
            )

            self.progress.set(1)

            self.status.configure(
                text="Decryption Completed Successfully"
            )

            messagebox.showinfo(
                "Success",
                "Image decrypted successfully."
            )

        except Exception as e:

            self.progress.set(0)

            messagebox.showerror(
                "Error",
                str(e)
            )