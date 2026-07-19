import hashlib


class Hashing:

    @staticmethod
    def sha256(filepath):

        sha = hashlib.sha256()

        with open(filepath, "rb") as file:

            while True:

                chunk = file.read(4096)

                if not chunk:

                    break

                sha.update(chunk)

        return sha.hexdigest()

    @staticmethod
    def sha512(filepath):

        sha = hashlib.sha512()

        with open(filepath, "rb") as file:

            while True:

                chunk = file.read(4096)

                if not chunk:

                    break

                sha.update(chunk)

        return sha.hexdigest()