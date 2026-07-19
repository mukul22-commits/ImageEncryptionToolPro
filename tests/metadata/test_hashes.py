from core.metadata.hash_calculator import HashCalculator

IMAGE = "samples/samples.jpg"

print()

print("MD5")
print(HashCalculator.md5(IMAGE))

print()

print("SHA256")
print(HashCalculator.sha256(IMAGE))

print()

print("SHA512")
print(HashCalculator.sha512(IMAGE))