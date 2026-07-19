from core.metadata.exif_reader import ExifReader

data = ExifReader.read(
    "samples/samples.jpg"
)

print()

for key, value in data.items():

    print(key, ":", value)