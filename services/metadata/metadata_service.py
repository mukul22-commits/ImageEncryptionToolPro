from core.metadata.metadata_reader import MetadataReader
from core.metadata.fileinfo import FileInfo
from core.metadata.hash_calculator import HashCalculator
from core.metadata.entropy import Entropy
from core.metadata.exif_reader import ExifReader
from core.metadata.risk import RiskAnalyzer


class MetadataService:

    @staticmethod
    def analyze(file_path):

        exif = ExifReader.read(file_path)

        return {

            "basic": MetadataReader.read(file_path),

            "file": FileInfo.read(file_path),

            "hashes": {

                "md5": HashCalculator.md5(file_path),

                "sha256": HashCalculator.sha256(file_path),

                "sha512": HashCalculator.sha512(file_path)

            },

            "entropy": Entropy.calculate(file_path),

            "risk": RiskAnalyzer.calculate(exif),

            "exif": exif

        }