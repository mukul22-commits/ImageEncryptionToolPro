from services.metadata.metadata_service import MetadataService
from services.export.csv_export import CsvExporter

data = MetadataService.analyze(
    "samples/samples.jpg"
)

path = CsvExporter.export(
    data,
    "exports/report.csv"
)

print(path)