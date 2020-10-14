getal1 = int(input("geef een eerste getal op"))
rest = getal1 % 2
# % is modulo rekenen : wat is de rest na deling door 2
if rest == 0:
    #waar -> even getal
    print(f"{getal1} is even")
else: 
    #onwaar -> onever getal
    print(f"{getal1} is oneven")

#alternatief
#!= is het verschillend van 0
if rest != 0:
    #onwaar -> onever getal
    print(f"{getal1} is oneven")
else: 
    #waar -> even getal
    print(f"{getal1} is even")
