from core.metadata.metadata_reader import MetadataReader

info = MetadataReader.read(
    "samples/samples.jpg"
)

for key, value in info.items():
    print(f"{key} : {value}")