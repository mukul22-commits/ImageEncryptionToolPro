import customtkinter as ctk

from gui.styles.colors import Colors


class HashCard(ctk.CTkFrame):

    def __init__(self, parent, title, value):

        super().__init__(
            parent,
            fg_color=Colors.CARD,
            corner_radius=15,
            border_width=1,
            border_color=Colors.BORDER
        )

        self.hash_value = value

        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 18, "bold"),
            text_color=Colors.PRIMARY
        )

        title_label.pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        self.textbox = ctk.CTkTextbox(
            self,
            height=70
        )

        self.textbox.pack(
            fill="x",
            padx=20
        )

        self.textbox.insert(
            "1.0",
            value
        )

        self.textbox.configure(
            state="disabled"
        )

        self.button = ctk.CTkButton(
            self,
            text="📋 Copy",
            command=self.copy_hash
        )

        self.button.pack(
            pady=15
        )

    def copy_hash(self):

        self.clipboard_clear()

        self.clipboard_append(
            self.hash_value
        )

        self.button.configure(
            text="✅ Copied"
        )