import customtkinter as ctk

from gui.components.progress_card import ProgressCard

app = ctk.CTk()

app.geometry("500x180")

card = ProgressCard(app)

card.pack(
    fill="x",
    padx=20,
    pady=20
)

card.update_progress(0.72)

app.mainloop()