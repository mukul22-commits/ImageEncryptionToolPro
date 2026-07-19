from pprint import pprint

from services.metadata.metadata_service import MetadataService

result = MetadataService.analyze(
    "samples/samples.jpg"
)

pprint(result)