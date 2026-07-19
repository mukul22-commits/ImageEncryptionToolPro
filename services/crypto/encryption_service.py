import os
import time

from core.aes import AES256
from services.history.history_service import HistoryService


class EncryptionService:

    @staticmethod
    def encrypt(input_file, output_file, password):

        start = time.time()

        result = AES256.encrypt_file(
            input_file,
            output_file,
            password
        )

        elapsed = round(time.time() - start, 3)

        HistoryService.log(
            output_file,
            operation="Encryption"
        )

        return {
            "success": result,
            "time": elapsed,
            "input_size": os.path.getsize(input_file),
            "output_size": os.path.getsize(output_file),
            "output": output_file
        }

    @staticmethod
    def decrypt(input_file, output_file, password):

        start = time.time()

        result = AES256.decrypt_file(
            input_file,
            output_file,
            password
        )

        elapsed = round(time.time() - start, 3)

        HistoryService.log(
            output_file,
            operation="Decryption"
        )

        return {
            "success": result,
            "time": elapsed,
            "input_size": os.path.getsize(input_file),
            "output_size": os.path.getsize(output_file),
            "output": output_file
        }