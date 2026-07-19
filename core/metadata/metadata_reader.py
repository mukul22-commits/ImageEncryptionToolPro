from pathlib import Path
from PIL import Image
import os


class MetadataReader:

    @staticmethod
    def read(file_path: str):

        image = Image.open(file_path)

        return {

            "filename": Path(file_path).name,

            "extension": Path(file_path).suffix,

            "format": image.format,

            "mode": image.mode,

            "width": image.width,

            "height": image.height,

            "filesize_kb": round(
                os.path.getsize(file_path) / 1024,
                2
            )

        }