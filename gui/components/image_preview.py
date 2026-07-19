import os
import customtkinter as ctk

from PIL import Image

from gui.styles.colors import Colors
from gui.styles.fonts import HEADING_FONT


class ImagePreview(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(

            parent,

            fg_color=Colors.CARD,

            corner_radius=15,

            border_width=1,

            border_color=Colors.BORDER

        )

        self.image_label = ctk.CTkLabel(

            self,

            text="No Image Selected",

            font=HEADING_FONT,

            text_color=Colors.SUBTEXT

        )

        self.image_label.pack(

            pady=20

        )

        self.info = ctk.CTkLabel(

            self,

            text="",

            text_color=Colors.TEXT

        )

        self.info.pack(

            pady=10

        )

    def load_image(self, image_path):

        try:

            image = Image.open(image_path)

            image.thumbnail((350, 350))

            ctk_image = ctk.CTkImage(

                light_image=image,

                dark_image=image,

                size=image.size

            )

            self.image_label.configure(

                image=ctk_image,

                text=""

            )

            self.image_label.image = ctk_image

            self.info.configure(

                text=f"{os.path.basename(image_path)}\n{image.width} × {image.height}"

            )

        except Exception as error:

            self.image_label.configure(

                text="Unable to Load Image",

                image=None

            )

            self.info.configure(

                text=str(error)

            )