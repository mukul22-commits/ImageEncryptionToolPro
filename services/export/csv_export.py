import csv
import os


class CsvExporter:

    @staticmethod
    def export(data, output_file):

        rows = []

        def flatten(prefix, obj):

            if isinstance(obj, dict):

                for key, value in obj.items():

                    flatten(
                        f"{prefix}.{key}" if prefix else key,
                        value
                    )

            else:

                rows.append(
                    [prefix, obj]
                )

        flatten("", data)

        with open(
            output_file,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                ["Field", "Value"]
            )

            writer.writerows(rows)

        return os.path.abspath(output_file)