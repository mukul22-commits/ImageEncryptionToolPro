import os

from database.db import Database
from core.hashing import Hashing


class HistoryService:

    _db = Database()

    @staticmethod
    def log(
        file_path,
        operation,
        algorithm="AES-256-GCM",
        status="Success"
    ):

        filename = os.path.basename(file_path)

        filesize = os.path.getsize(file_path)

        sha256 = Hashing.sha256(file_path)

        HistoryService._db.insert(
            filename=filename,
            algorithm=algorithm,
            operation=operation,
            filesize=filesize,
            sha256=sha256,
            status=status
        )

    @staticmethod
    def fetch():

        return HistoryService._db.fetch()

    # =====================================
    # Dashboard Statistics
    # =====================================

    @staticmethod
    def total():

        return HistoryService._db.count_all()

    @staticmethod
    def encrypted():

        return HistoryService._db.count_encrypt()

    @staticmethod
    def decrypted():

        return HistoryService._db.count_decrypt()

    @staticmethod
    def processed_size():

        return HistoryService._db.total_size()

    @staticmethod
    def success():

        return HistoryService._db.success_count()

    @staticmethod
    def failed():

        return HistoryService._db.failed_count()

    @staticmethod
    def recent(limit=5):

        return HistoryService._db.recent(limit)