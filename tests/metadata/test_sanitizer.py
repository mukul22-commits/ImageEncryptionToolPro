from core.metadata.sanitizer import MetadataSanitizer

output = MetadataSanitizer.remove_metadata(
    "samples/samples.jpg"
)

print("Sanitized Image")

print(output)