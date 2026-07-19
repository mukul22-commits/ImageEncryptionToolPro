from reportlab.platypus import SimpleDocTemplate, Paragraph  # type: ignore[import]
from reportlab.lib.styles import getSampleStyleSheet  # type: ignore[import]


class PdfExporter:

    @staticmethod
    def export(data, output_file):

        styles = getSampleStyleSheet()

        doc = SimpleDocTemplate(output_file)

        story = []

        story.append(
            Paragraph(
                "<b>ImageShield Pro Report</b>",
                styles["Heading1"]
            )
        )

        def add(prefix, obj):

            if isinstance(obj, dict):

                for k, v in obj.items():

                    add(
                        f"{prefix}.{k}" if prefix else k,
                        v
                    )

            else:

                story.append(
                    Paragraph(
                        f"<b>{prefix}</b> : {obj}",
                        styles["BodyText"]
                    )
                )

        add("", data)

        doc.build(story)

        return output_file