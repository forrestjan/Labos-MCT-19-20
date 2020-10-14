def toon_max(getal1, getal2, getal3):
    if getal1 > getal2 and getal1 > getal3:
        return getal1
    elif getal2 > getal3 and getal2 > getal1:
        return getal2
    else:
        return getal3
    #return max(getal1, getal2, Getal3)

print(f"het grootste getal is: {toon_max(3.14, 3345453, -7)}")