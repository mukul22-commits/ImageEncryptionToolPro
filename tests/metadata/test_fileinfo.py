from core.metadata.fileinfo import FileInfo

info = FileInfo.read(
    "samples/samples.jpg"
)

print()

for key, value in info.items():

    print(key, ":", value)