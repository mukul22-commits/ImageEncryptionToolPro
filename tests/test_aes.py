from pathlib import Path

from core.aes import AES256

PASSWORD = "Cyber@123"

INPUT_FILE = "samples/samples.jpg"

OUTPUT_DIR = "output"

encrypted = str(
    Path(OUTPUT_DIR) / "sample.enc"
)

decrypted = str(
    Path(OUTPUT_DIR) / "sample_decrypted.jpg"
)

enc = AES256.encrypt_file(

    INPUT_FILE,

    encrypted,

    PASSWORD

)

dec = AES256.decrypt_file(

    encrypted,

    decrypted,

    PASSWORD

)

print()

print("Encryption Successful")

print(enc)

print()

print("Decryption Successful")

print(dec)