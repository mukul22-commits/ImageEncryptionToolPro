import customtkinter as ctk

from gui.components.status_bar import StatusBar

app = ctk.CTk()

app.geometry("600x120")

bar = StatusBar(app)

bar.pack(
    fill="x",
    side="bottom"
)

bar.set_status(
    "Metadata Loaded Successfully"
)

app.mainloop()