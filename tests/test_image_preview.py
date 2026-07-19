import customtkinter as ctk

from gui.components.image_preview import ImagePreview

app = ctk.CTk()

app.geometry("500x550")

preview = ImagePreview(app)

preview.pack(

    fill="both",

    expand=True,

    padx=20,

    pady=20

)

preview.load_image(

    "samples/samples.jpg"

)

app.mainloop()