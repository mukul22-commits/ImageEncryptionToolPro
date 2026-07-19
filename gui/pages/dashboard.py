import customtkinter as ctk

from utils.theme import Theme


class Dashboard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent, fg_color=Theme.BG)

        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Segoe UI", 30, "bold"),
            text_color=Theme.PRIMARY
        )

        title.pack(pady=(10, 20))

        cards = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        cards.pack(fill="x", padx=20)

        data = [

            ("Encrypted", "0"),

            ("Decrypted", "0"),

            ("History", "0"),

            ("Algorithm", "AES-256")

        ]

        for text, value in data:

            card = ctk.CTkFrame(
                cards,
                width=220,
                height=120,
                corner_radius=15
            )

            card.pack(
                side="left",
                padx=10,
                pady=10,
                expand=True,
                fill="both"
            )

            ctk.CTkLabel(
                card,
                text=text,
                font=("Segoe UI", 16)
            ).pack(pady=(20, 5))

            ctk.CTkLabel(
                card,
                text=value,
                font=("Segoe UI", 24, "bold"),
                text_color=Theme.PRIMARY
            ).pack()