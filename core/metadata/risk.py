class RiskAnalyzer:

    @staticmethod
    def calculate(metadata):

        score = 0
        reasons = []

        if "GPSInfo" in metadata:
            score += 30
            reasons.append("GPS coordinates detected")

        if "Software" in metadata:
            score += 10
            reasons.append("Image editing software detected")

        if "Artist" in metadata:
            score += 10
            reasons.append("Author information detected")

        if "Copyright" in metadata:
            score += 5
            reasons.append("Copyright metadata detected")

        if score == 0:
            reasons.append("No privacy risks detected")

        if score <= 20:
            level = "Low"

        elif score <= 50:
            level = "Medium"

        else:
            level = "High"

        return {

            "Risk Score": score,

            "Risk Level": level,

            "Reasons": reasons

        }