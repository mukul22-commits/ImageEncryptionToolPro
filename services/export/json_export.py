import json
import os


class JsonExporter:

    @staticmethod
    def export(data, output_path):

        def serialize(obj):

            if hasattr(obj, "isoformat"):
                return obj.isoformat()

            return str(obj)

        with open(

            output_path,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                data,

                file,

                indent=4,

                default=serialize

            )

        return os.path.abspath(output_path)