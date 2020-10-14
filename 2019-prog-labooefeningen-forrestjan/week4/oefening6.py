klinkers = []
medeklinkers = []
lijst_klinkers = ['a', 'e', 'i', 'o', 'u', 'y']

woord = input("geef een woord > ")

for letter in woord.lower():
    if letter in lijst_klinkers:
        klinkers.append(letter)
    else:
        medeklinkers.append(letter)

print(f"De gevonden klinkers zijn: {klinkers}")
print(f"De gevonden medeklinkers zijn: {medeklinkers}")
