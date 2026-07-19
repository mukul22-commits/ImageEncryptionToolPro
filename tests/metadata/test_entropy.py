from core.metadata.entropy import Entropy

value = Entropy.calculate(
    "samples/samples.jpg"
)

print()

print("Entropy :", value)