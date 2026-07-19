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