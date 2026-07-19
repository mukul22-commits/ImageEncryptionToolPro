import os

from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


SALT_SIZE = 16
KEY_SIZE = 32
ITERATIONS = 200000


def generate_salt():
    return os.urandom(SALT_SIZE)


def derive_key(password: str, salt: bytes) -> bytes:

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=ITERATIONS,
    )

    return kdf.derive(password.encode())