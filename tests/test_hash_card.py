import customtkinter as ctk

from gui.components.hash_card import HashCard


app = ctk.CTk()

app.title("Hash Card")

app.geometry("900x300")


hash_value = (
    "2a9883868d61897978130ae68074435e"
    "28a859d0c191d3ade7e8685ee1bff130"
)


card = HashCard(

    app,

    "SHA-256",

    hash_value

)

card.pack(

    fill="both",

    expand=True,

    padx=20,

    pady=20

)

app.mainloop()