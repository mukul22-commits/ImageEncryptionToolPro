import customtkinter as ctk

from gui.components.security_card import SecurityCard

app = ctk.CTk()

app.geometry("350x250")

card = SecurityCard(app)

card.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

card.update_score(92)

app.mainloop()