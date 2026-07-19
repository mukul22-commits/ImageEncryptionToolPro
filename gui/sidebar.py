import customtkinter as ctk

from utils.theme import Theme


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent, callback):

        super().__init__(
            parent,
            width=Theme.SIDEBAR_WIDTH,
            fg_color=Theme.CARD,
            corner_radius=0
        )

        self.callback = callback

        self.pack_propagate(False)

        # ==========================
        # Logo / Title
        # ==========================

        logo = ctk.CTkLabel(
            self,
            text="🔐 Image Encryption",
            font=("Segoe UI", 24, "bold"),
            text_color=Theme.PRIMARY
        )

        logo.pack(
            pady=(30, 8)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Tool Pro v3.0",
            font=("Segoe UI", 13),
            text_color=Theme.SUBTEXT
        )

        subtitle.pack(
            pady=(0, 25)
        )

        # ==========================
        # Navigation Buttons
        # ==========================

        self.pages = [

            ("🏠", "Dashboard"),

            ("🔐", "Encrypt"),

            ("🔓", "Decrypt"),

            ("📦", "Batch"),

            ("📜", "History"),

            ("📊", "Analytics"),

            ("📄", "Reports"),

            ("⚙", "Settings"),

            ("ℹ", "About")

        ]

        self.buttons = {}

        for icon, page in self.pages:

            btn = ctk.CTkButton(

                self,

                text=f"{icon}   {page}",

                height=45,

                corner_radius=12,

                font=("Segoe UI", 15),

                fg_color="transparent",

                hover_color="#1E293B",

                text_color="white",

                anchor="w",

                command=lambda p=page: self.select_page(p)

            )

            btn.pack(

                fill="x",

                padx=15,

                pady=6

            )

            self.buttons[page] = btn

        # Highlight Dashboard initially
        self.highlight("Dashboard")

        # ==========================
        # Bottom Section
        # ==========================

        bottom = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        bottom.pack(
            side="bottom",
            fill="x",
            pady=20
        )

        version = ctk.CTkLabel(

            bottom,

            text="Version 3.0",

            font=("Segoe UI", 12),

            text_color=Theme.SUBTEXT

        )

        version.pack()

        author = ctk.CTkLabel(

            bottom,

            text="© Mukul Sharma",

            font=("Segoe UI", 11),

            text_color=Theme.SUBTEXT

        )

        author.pack(
            pady=(5, 0)
        )

    # ==========================
    # Highlight Selected Button
    # ==========================

    def highlight(self, selected):

        for page, button in self.buttons.items():

            if page == selected:

                button.configure(

                    fg_color=Theme.PRIMARY,

                    text_color="black"

                )

            else:

                button.configure(

                    fg_color="transparent",

                    text_color="white"

                )

    # ==========================
    # Handle Navigation
    # ==========================

    def select_page(self, page):

        self.highlight(page)

        self.callback(page)