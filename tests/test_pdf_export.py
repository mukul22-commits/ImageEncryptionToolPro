from services.metadata.metadata_service import MetadataService
from services.export.pdf_export import PdfExporter

data = MetadataService.analyze(
    "samples/samples.jpg"
)

PdfExporter.export(
    data,
    "exports/report.pdf"
)

print("PDF Created")