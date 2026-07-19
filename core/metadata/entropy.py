import math


class Entropy:

    @staticmethod
    def calculate(file_path):

        with open(file_path, "rb") as file:

            data = file.read()

        if len(data) == 0:

            return 0

        frequency = [0] * 256

        for byte in data:

            frequency[byte] += 1

        entropy = 0

        data_length = len(data)

        for count in frequency:

            if count == 0:

                continue

            probability = count / data_length

            entropy -= probability * math.log2(probability)

        return round(entropy, 4)