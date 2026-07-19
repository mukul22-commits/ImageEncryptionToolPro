import customtkinter as ctk

from gui.components.metadata_table import MetadataTable

from services.metadata.metadata_service import MetadataService

app = ctk.CTk()

app.geometry("900x650")

table = MetadataTable(app)

table.pack(

    fill="both",

    expand=True,

    padx=20,

    pady=20

)

result = MetadataService.analyze(

    "samples/samples.jpg"

)

table.load(

    result

)

app.mainloop()