class SecurityScore:

    @staticmethod
    def calculate(metadata):

        score = 100

        exif = metadata.get("exif", {})

        if exif:
            score -= 15

        risk = metadata.get("risk", {})

        score -= risk.get("Risk Score", 0)

        return max(score, 0)