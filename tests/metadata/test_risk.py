from core.metadata.exif_reader import ExifReader
from core.metadata.risk import RiskAnalyzer

metadata = ExifReader.read(
    "samples/samples.jpg"
)

result = RiskAnalyzer.calculate(metadata)

print()

for key, value in result.items():

    print(key, ":", value)