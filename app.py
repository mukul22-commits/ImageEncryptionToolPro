import customtkinter as ctk

from utils.theme import Theme

from gui.sidebar import Sidebar
from gui.header import Header

from gui.pages.dashboard import Dashboard
from gui.pages.encrypt import EncryptPage
from gui.pages.decrypt import DecryptPage
from gui.pages.metadata import MetadataPage
from gui.pages.history import HistoryPage


class ImageEncryptionApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ==========================
        # Window Configuration
        # ==========================

        self.title(f"{Theme.APP_NAME} v{Theme.VERSION}")
        self.geometry(f"{Theme.WIDTH}x{Theme.HEIGHT}")
        self.minsize(1200, 800)
        self.configure(fg_color=Theme.BG)

        # ==========================
        # Sidebar
        # ==========================

        self.sidebar = Sidebar(
            self,
            self.change_page
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        # ==========================
        # Main Container
        # ==========================

        self.main = ctk.CTkFrame(
            self,
            fg_color=Theme.BG
        )

        self.main.pack(
            side="right",
            fill="both",
            expand=True
        )

        # ==========================
        # Header
        # ==========================

        self.header = Header(self.main)

        self.header.pack(
            fill="x"
        )

        # ==========================
        # Content Area
        # ==========================

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

        # Open Dashboard

        self.change_page("Dashboard")

    # ==================================================
    # Clear Current Page
    # ==================================================

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    # ==================================================
    # Page Navigation
    # ==================================================

    def change_page(self, page):

        self.clear_content()

        page_map = {

            "Dashboard": Dashboard,

            "Encrypt": EncryptPage,

            "Decrypt": DecryptPage,

            "Metadata Inspector": MetadataPage,

	    "History": HistoryPage,

        }

        if page in page_map:

            page_map[page](self.content).pack(
                fill="both",
                expand=True
            )

        else:

            self.show_placeholder(page)

    # ==================================================
    # Placeholder Pages
    # ==================================================

    def show_placeholder(self, page):

        frame = ctk.CTkFrame(
            self.content,
            fg_color=Theme.CARD,
            corner_radius=15
        )

        frame.pack(
            fill="both",
            expand=True
        )

        ctk.CTkLabel(
            frame,
            text=page,
            font=("Segoe UI", 30, "bold"),
            text_color=Theme.PRIMARY
        ).pack(
            pady=(80, 20)
        )

        ctk.CTkLabel(
            frame,
            text="This module is under development.",
            font=("Segoe UI", 18),
            text_color=Theme.SUBTEXT
        ).pack()

        ctk.CTkLabel(
            frame,
            text="ImageEncryptionToolPro v3.0",
            font=("Segoe UI", 14),
            text_color="gray"
        ).pack(
            pady=15
        )


# ==================================================
# Main
# ==================================================

if __name__ == "__main__":

    ctk.set_appearance_mode("Dark")

    ctk.set_default_color_theme("blue")

    app = ImageEncryptionApp()

    app.mainloop()