from core.metadata.exif_reader import ExifReader

print("Original EXIF")

print(
    ExifReader.read(
        "samples/samples.jpg"
    )
)

print()

print("Clean EXIF")

print(
    ExifReader.read(
        "output/samples_clean.jpg"
    )
)