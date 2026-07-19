import customtkinter as ctk

from utils.theme import Theme

from gui.sidebar import Sidebar
from gui.header import Header

from gui.pages.dashboard import Dashboard


class AppWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title(
            f"{Theme.APP_NAME} v{Theme.VERSION}"
        )

        self.geometry(
            f"{Theme.WIDTH}x{Theme.HEIGHT}"
        )

        self.minsize(
            1300,
            850
        )

        self.configure(
            fg_color=Theme.BG
        )

        self.sidebar = Sidebar(
            self,
            self.change_page
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.main = ctk.CTkFrame(
            self,
            fg_color=Theme.BG
        )

        self.main.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.header = Header(
            self.main
        )

        self.header.pack(
            fill="x"
        )

        self.content = ctk.CTkFrame(
            self.main,
            fg_color=Theme.BG
        )

        self.content.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.change_page("Dashboard")

    def clear(self):

        for widget in self.content.winfo_children():

            widget.destroy()

    def change_page(self, page):

        self.clear()

        if page == "Dashboard":

            Dashboard(self.content).pack(
                fill="both",
                expand=True
            )

        else:

            ctk.CTkLabel(

                self.content,

                text=f"{page}\nComing Soon",

                font=Theme.TITLE,

                text_color=Theme.PRIMARY

            ).pack(
                pady=100
            )