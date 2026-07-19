import customtkinter as ctk

from gui.styles.colors import Colors


class StatusBar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=Colors.CARD,
            height=35,
            corner_radius=0
        )

        self.pack_propagate(False)

        self.label = ctk.CTkLabel(
            self,
            text="Ready",
            anchor="w",
            text_color=Colors.TEXT,
            font=("Segoe UI", 12)
        )

        self.label.pack(
            side="left",
            padx=15
        )

    def set_status(self, message):

        self.label.configure(
            text=message
        )