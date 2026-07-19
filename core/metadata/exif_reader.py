from PIL import Image
from PIL.ExifTags import TAGS


class ExifReader:

    @staticmethod
    def read(file_path):

        result = {}

        try:

            image = Image.open(file_path)

            exif = image.getexif()

            if exif:

                for tag, value in exif.items():

                    name = TAGS.get(tag, tag)

                    result[name] = value

        except Exception:

            pass

        return result