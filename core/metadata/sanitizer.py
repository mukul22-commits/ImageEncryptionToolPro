from PIL import Image
import os


class MetadataSanitizer:

    @staticmethod
    def remove_metadata(input_file, output_file=None):

        image = Image.open(input_file)

        data = list(image.getdata())

        clean = Image.new(
            image.mode,
            image.size
        )

        clean.putdata(data)

        if output_file is None:

            filename = os.path.basename(input_file)

            name, ext = os.path.splitext(filename)

            output_file = os.path.join(
                "output",
                f"{name}_clean{ext}"
            )

        os.makedirs(
            os.path.dirname(output_file),
            exist_ok=True
        )

        clean.save(output_file)

        return output_file