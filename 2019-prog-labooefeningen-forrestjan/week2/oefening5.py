#Vraag de decimale score (op 20) van een module aan de gebruiker. Print nadien af of hij/zij geslaagd is. Zorg
#ervoor dat de score correct afgerond wordt: indien het decimale gedeelte kleiner is dan 0,5 wordt er naar
#beneden afgerond. In het andere geval wordt er naar boven afgerond. Print ook de afgeronde score af.
from math import ceil, floor

score = float(input("geef je score op 20: "))
#waarde_na_de_komma WORDT 18.5 - 18 dus 0.5(want float word omgezet nar int en rond dus af naar beneden)
waarde_na_de_komma = score - int(score)

if waarde_na_de_komma < 0.5:
    afgerond = floor (score)
    
else:
    afgerond = ceil(score)

print(f"je nieuwe punt is {afgerond}")

if afgerond >= 10:
    print("U bent geslaagd")

else:
    print("U bent niet geslaagd")