import os
import time

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from core.key_derivation import derive_key, generate_salt
from utils.logger import logger


SALT_SIZE = 16
NONCE_SIZE = 12


class AES256:

    @staticmethod
    def encrypt_file(
        input_file: str,
        output_file: str,
        password: str
    ):

        if not os.path.isfile(input_file):
            raise FileNotFoundError(
                f"{input_file} does not exist."
            )

        if len(password) < 8:
            raise ValueError(
                "Password must contain at least 8 characters."
            )

        os.makedirs(
            os.path.dirname(output_file),
            exist_ok=True
        )

        start = time.time()

        salt = generate_salt()

        key = derive_key(password, salt)

        nonce = os.urandom(NONCE_SIZE)

        aes = AESGCM(key)

        with open(input_file, "rb") as file:

            plaintext = file.read()

        ciphertext = aes.encrypt(
            nonce,
            plaintext,
            None
        )

        with open(output_file, "wb") as file:

            file.write(salt)
            file.write(nonce)
            file.write(ciphertext)

        elapsed = round(
            time.time() - start,
            3
        )

        logger.info(
            f"Encrypted : {input_file}"
        )

        return {

            "success": True,

            "time": elapsed,

            "size": os.path.getsize(output_file)

        }

    @staticmethod
    def decrypt_file(
        input_file: str,
        output_file: str,
        password: str
    ):

        if not os.path.isfile(input_file):
            raise FileNotFoundError(
                f"{input_file} does not exist."
            )

        start = time.time()

        with open(input_file, "rb") as file:

            salt = file.read(SALT_SIZE)

            nonce = file.read(NONCE_SIZE)

            ciphertext = file.read()

        key = derive_key(
            password,
            salt
        )

        aes = AESGCM(key)

        plaintext = aes.decrypt(
            nonce,
            ciphertext,
            None
        )

        os.makedirs(
            os.path.dirname(output_file),
            exist_ok=True
        )

        with open(output_file, "wb") as file:

            file.write(plaintext)

        elapsed = round(
            time.time() - start,
            3
        )

        logger.info(
            f"Decrypted : {input_file}"
        )

        return {

            "success": True,

            "time": elapsed,

            "size": os.path.getsize(output_file)

        }