from services.metadata.metadata_service import MetadataService

from services.export.json_export import JsonExporter

data = MetadataService.analyze(

    "samples/samples.jpg"

)

output = JsonExporter.export(

    data,

    "exports/report.json"

)

print(output)