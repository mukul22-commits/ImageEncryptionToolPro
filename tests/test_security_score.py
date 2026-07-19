from services.metadata.metadata_service import MetadataService

from core.security.score import SecurityScore

result = MetadataService.analyze(
    "samples/samples.jpg"
)

print(

    SecurityScore.calculate(
        result
    )

)