import customtkinter as ctk

from utils.theme import Theme


class Header(ctk.CTkFrame):

    def __init__(

        self,

        parent

    ):

        super().__init__(

            parent,

            height=Theme.HEADER_HEIGHT,

            fg_color=Theme.CARD

        )

        self.pack_propagate(False)

        title = ctk.CTkLabel(

            self,

            text="Image Encryption Tool Pro v3.0",

            font=Theme.TITLE,

            text_color=Theme.PRIMARY

        )

        title.pack(

            pady=15

        )