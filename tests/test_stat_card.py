import customtkinter as ctk

from gui.components.stat_card import StatCard

app = ctk.CTk()

app.title("Stat Card Test")

app.geometry("300x180")

card = StatCard(
    app,
    "Encrypted Files",
    "125"
)

card.pack(
    padx=20,
    pady=20,
    fill="both",
    expand=True
)

app.mainloop()