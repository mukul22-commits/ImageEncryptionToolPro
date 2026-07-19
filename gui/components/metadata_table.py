import customtkinter as ctk

from gui.styles.colors import Colors
from gui.styles.fonts import BODY_FONT


class MetadataTable(ctk.CTkScrollableFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=Colors.CARD,
            corner_radius=15,
            border_width=1,
            border_color=Colors.BORDER
        )

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

    def clear(self):

        for widget in self.winfo_children():
            widget.destroy()

    def add_section(self, title, row):

        section = ctk.CTkLabel(
            self,
            text=title.upper(),
            font=("Segoe UI", 18, "bold"),
            text_color=Colors.ACCENT
        )

        section.grid(
            row=row,
            column=0,
            columnspan=2,
            sticky="w",
            padx=10,
            pady=(15, 8)
        )

        return row + 1

    def add_row(self, key, value, row):

        key_label = ctk.CTkLabel(
            self,
            text=str(key),
            width=180,
            anchor="w",
            font=("Segoe UI", 13, "bold"),
            text_color=Colors.PRIMARY
        )

        key_label.grid(
            row=row,
            column=0,
            sticky="nw",
            padx=10,
            pady=4
        )

        value_box = ctk.CTkTextbox(
            self,
            height=28,
            border_width=0
        )

        value_box.grid(
            row=row,
            column=1,
            sticky="ew",
            padx=10,
            pady=4
        )

        value_box.insert(
            "1.0",
            str(value)
        )

        value_box.configure(
            state="disabled"
        )

        return row + 1

    def load(self, metadata):

        self.clear()

        row = 0

        for section, values in metadata.items():

            row = self.add_section(section, row)

            if isinstance(values, dict):

                for key, value in values.items():

                    row = self.add_row(
                        key,
                        value,
                        row
                    )

            else:

                row = self.add_row(
                    section,
                    values,
                    row
                )