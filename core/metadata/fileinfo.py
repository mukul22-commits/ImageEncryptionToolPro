import os
import mimetypes

from datetime import datetime


class FileInfo:

    @staticmethod
    def read(file_path):

        stat = os.stat(file_path)

        return {

            "File Name":
                os.path.basename(file_path),

            "Absolute Path":
                os.path.abspath(file_path),

            "Extension":
                os.path.splitext(file_path)[1],

            "MIME Type":
                mimetypes.guess_type(file_path)[0],

            "File Size (KB)":
                round(stat.st_size / 1024, 2),

            "Created":
                datetime.fromtimestamp(
                    stat.st_ctime
                ),

            "Modified":
                datetime.fromtimestamp(
                    stat.st_mtime
                )

        }