import customtkinter as ctk

from gui.styles.colors import Colors


class ProgressCard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=Colors.CARD,
            corner_radius=15,
            border_width=1,
            border_color=Colors.BORDER
        )

        ctk.CTkLabel(
            self,
            text="Progress",
            font=("Segoe UI", 18, "bold"),
            text_color=Colors.PRIMARY
        ).pack(
            pady=(15, 10)
        )

        self.progress = ctk.CTkProgressBar(self)

        self.progress.pack(
            fill="x",
            padx=20,
            pady=15
        )

        self.progress.set(0)

        self.label = ctk.CTkLabel(
            self,
            text="0%",
            text_color=Colors.TEXT
        )

        self.label.pack(
            pady=(0, 15)
        )

    def update_progress(self, value):

        self.progress.set(value)

        self.label.configure(
            text=f"{int(value*100)}%"
        )