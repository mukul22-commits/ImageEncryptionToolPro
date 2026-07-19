import customtkinter as ctk

from gui.components.risk_card import RiskCard

app = ctk.CTk()

app.geometry("420x350")

risk = {

    "Risk Score": 0,

    "Risk Level": "Low",

    "Reasons": [

        "No privacy risks detected"

    ]

}

card = RiskCard(

    app,

    risk

)

card.pack(

    fill="both",

    expand=True,

    padx=20,

    pady=20

)

app.mainloop()