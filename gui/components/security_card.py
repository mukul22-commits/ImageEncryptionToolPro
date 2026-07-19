import customtkinter as ctk

from gui.styles.colors import Colors


class SecurityCard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=Colors.CARD,
            corner_radius=15,
            border_width=1,
            border_color=Colors.BORDER
        )

        self.title = ctk.CTkLabel(
            self,
            text="Security Score",
            font=("Segoe UI",18,"bold"),
            text_color=Colors.PRIMARY
        )

        self.title.pack(pady=(15,5))

        self.score = ctk.CTkLabel(
            self,
            text="0 / 100",
            font=("Segoe UI",34,"bold"),
            text_color=Colors.SUCCESS
        )

        self.score.pack()

        self.message = ctk.CTkLabel(
            self,
            text="Waiting for analysis...",
            text_color=Colors.SUBTEXT
        )

        self.message.pack(pady=15)

    def update_score(self, score):

        self.score.configure(
            text=f"{score}/100"
        )

        if score >= 80:

            color = Colors.SUCCESS
            msg = "Excellent"

        elif score >= 60:

            color = Colors.WARNING
            msg = "Average"

        else:

            color = Colors.DANGER
            msg = "Needs Attention"

        self.score.configure(
            text_color=color
        )

        self.message.configure(
            text=msg
        )