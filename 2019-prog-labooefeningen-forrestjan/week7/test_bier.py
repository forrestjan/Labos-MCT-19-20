# Test class Bier
from model.Bier import Bier

print("** Bier 1 ***")
b1 = Bier("Augustijn", "Bios", 12.0, "amber")
print(b1)
# verander de brouwerij naar lege string
b1.brouwerij = ""
print(b1)

print("** Bier 2 ***")
b2 = Bier("Jupiler", "", 3.3, "blond")
print(f"Het kleur van {b2.naam} is {b2.kleur} ")
print(f"Alcoholpercentage: {b2.alcoholpercentage} ")
b2.alcoholpercentage = "5,5"
print(f"Alcoholpercentage: {b2.alcoholpercentage} ")
