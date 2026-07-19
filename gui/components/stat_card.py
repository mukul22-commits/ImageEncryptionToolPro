import customtkinter as ctk

from gui.styles.colors import Colors
from gui.styles.fonts import HEADING_FONT, BODY_FONT


class StatCard(ctk.CTkFrame):

    def __init__(self, parent, title, value, color=Colors.PRIMARY):

        super().__init__(

            parent,

            fg_color=Colors.CARD,

            corner_radius=15,

            border_width=1,

            border_color=Colors.BORDER,

            width=220,

            height=120

        )

        self.pack_propagate(False)

        ctk.CTkLabel(

            self,

            text=title,

            font=BODY_FONT,

            text_color=Colors.SUBTEXT

        ).pack(

            pady=(20, 5)

        )

        self.value = ctk.CTkLabel(

            self,

            text=value,

            font=HEADING_FONT,

            text_color=color

        )

        self.value.pack()

    def update_value(self, value):

        self.value.configure(

            text=value

        )