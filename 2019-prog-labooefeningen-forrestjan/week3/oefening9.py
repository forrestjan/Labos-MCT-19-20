from random import randint

rand_getal = randint(1, 20)

gokje = int(input("Doe een gokje van 1 tot 20 > "))

while gokje != rand_getal:
    if rand_getal > gokje:
        print("hoger!")
    else:
        print("Lager!")
    gokje = int(input("Doe een gokje van 1 tot 20 > "))

print(f"Het getal is inderdaad {rand_getal}")
