import hashlib


class HashCalculator:

    @staticmethod
    def md5(file_path):

        md5 = hashlib.md5()

        with open(file_path, "rb") as file:

            while True:

                chunk = file.read(4096)

                if not chunk:
                    break

                md5.update(chunk)

        return md5.hexdigest()

    @staticmethod
    def sha256(file_path):

        sha = hashlib.sha256()

        with open(file_path, "rb") as file:

            while True:

                chunk = file.read(4096)

                if not chunk:
                    break

                sha.update(chunk)

        return sha.hexdigest()

    @staticmethod
    def sha512(file_path):

        sha = hashlib.sha512()

        with open(file_path, "rb") as file:

            while True:

                chunk = file.read(4096)

                if not chunk:
                    break

                sha.update(chunk)

        return sha.hexdigest()