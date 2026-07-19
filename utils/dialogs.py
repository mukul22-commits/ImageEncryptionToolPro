from tkinter import filedialog


def open_image():

    return filedialog.askopenfilename(

        title="Select Image",

        filetypes=[

            ("Images",

             "*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.webp")

        ]

    )


def save_file():

    return filedialog.asksaveasfilename()