from PIL import Image


class Thumbnail:

    @staticmethod
    def create(

        image_path,

        output,

        size=(250, 250)

    ):

        image = Image.open(image_path)

        image.thumbnail(size)

        image.save(output)

        return output