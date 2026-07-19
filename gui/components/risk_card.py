import customtkinter as ctk

from gui.styles.colors import Colors
from gui.styles.fonts import HEADING_FONT, BODY_FONT


class RiskCard(ctk.CTkFrame):

    def __init__(self, parent, risk_data):

        super().__init__(
            parent,
            fg_color=Colors.CARD,
            corner_radius=15,
            border_width=1,
            border_color=Colors.BORDER
        )

        score = risk_data["Risk Score"]
        level = risk_data["Risk Level"]
        reasons = risk_data["Reasons"]

        if level == "Low":
            color = Colors.SUCCESS
        elif level == "Medium":
            color = Colors.WARNING
        else:
            color = Colors.DANGER

        ctk.CTkLabel(
            self,
            text="Privacy Risk",
            font=HEADING_FONT,
            text_color=Colors.PRIMARY
        ).pack(pady=(15, 5))

        self.level = ctk.CTkLabel(
            self,
            text=level,
            font=("Segoe UI", 30, "bold"),
            text_color=color
        )

        self.level.pack()

        ctk.CTkLabel(
            self,
            text=f"Risk Score : {score}",
            font=BODY_FONT,
            text_color=Colors.TEXT
        ).pack(pady=(5, 15))

        for reason in reasons:

            ctk.CTkLabel(
                self,
                text="• " + reason,
                anchor="w",
                justify="left",
                font=BODY_FONT,
                text_color=Colors.SUBTEXT
            ).pack(
                fill="x",
                padx=20
            )