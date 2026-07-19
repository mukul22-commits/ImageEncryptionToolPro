import os


class Validator:

    VALID = {

        ".jpg",

        ".jpeg",

        ".png",

        ".bmp",

        ".gif",

        ".tiff",

        ".webp"

    }

    @staticmethod
    def validate(file):

        if not os.path.isfile(file):

            return False

        extension = os.path.splitext(file)[1].lower()

        return extension in Validator.VALID