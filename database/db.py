import sqlite3

from utils.constants import DATABASE


class Database:

    def __init__(self):
        self.conn = sqlite3.connect(DATABASE)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS history(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                filename TEXT,

                algorithm TEXT,

                operation TEXT,

                filesize INTEGER,

                sha256 TEXT,

                status TEXT,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )
            """
        )

        self.conn.commit()

    def insert(
        self,
        filename,
        algorithm,
        operation,
        filesize,
        sha256,
        status
    ):

        self.cursor.execute(
            """
            INSERT INTO history(

                filename,
                algorithm,
                operation,
                filesize,
                sha256,
                status

            )

            VALUES(?,?,?,?,?,?)
            """,
            (
                filename,
                algorithm,
                operation,
                filesize,
                sha256,
                status
            )
        )

        self.conn.commit()

    def fetch(self):

        self.cursor.execute(
            "SELECT * FROM history ORDER BY id DESC"
        )

        return self.cursor.fetchall()

    # ===============================
    # Dashboard Statistics
    # ===============================

    def count_all(self):

        self.cursor.execute(
            "SELECT COUNT(*) FROM history"
        )

        return self.cursor.fetchone()[0]

    def count_encrypt(self):

        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM history
            WHERE operation='Encryption'
            """
        )

        return self.cursor.fetchone()[0]

    def count_decrypt(self):

        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM history
            WHERE operation='Decryption'
            """
        )

        return self.cursor.fetchone()[0]

    def total_size(self):

        self.cursor.execute(
            """
            SELECT IFNULL(SUM(filesize),0)
            FROM history
            """
        )

        return self.cursor.fetchone()[0]

    def success_count(self):

        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM history
            WHERE status='Success'
            """
        )

        return self.cursor.fetchone()[0]

    def failed_count(self):

        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM history
            WHERE status!='Success'
            """
        )

        return self.cursor.fetchone()[0]

    def recent(self, limit=5):

        self.cursor.execute(
            """
            SELECT
                operation,
                filename,
                created_at

            FROM history

            ORDER BY id DESC

            LIMIT ?
            """,
            (limit,)
        )

        return self.cursor.fetchall()