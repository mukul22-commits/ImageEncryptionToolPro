import customtkinter as ctk

from services.history.history_service import HistoryService
from utils.theme import Theme


class HistoryPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent, fg_color=Theme.BG)

        ctk.CTkLabel(
            self,
            text="Encryption History",
            font=("Segoe UI", 28, "bold"),
            text_color=Theme.PRIMARY
        ).pack(pady=(20,10))

        self.textbox = ctk.CTkTextbox(
            self,
            width=1000,
            height=550
        )

        self.textbox.pack(
            padx=20,
            pady=20,
            fill="both",
            expand=True
        )

        ctk.CTkButton(
            self,
            text="Refresh",
            command=self.load_history
        ).pack(pady=10)

        self.load_history()

    def load_history(self):

        self.textbox.delete("1.0", "end")

        rows = HistoryService.fetch()

        if not rows:
            self.textbox.insert("end", "No history found.")
            return

        for row in rows:

            self.textbox.insert(
                "end",
                f"""
ID         : {row[0]}
Filename   : {row[1]}
Algorithm  : {row[2]}
Operation  : {row[3]}
Size       : {row[4]} bytes
SHA256     : {row[5]}
Status     : {row[6]}
Date       : {row[7]}

------------------------------------------------------------

"""
            )