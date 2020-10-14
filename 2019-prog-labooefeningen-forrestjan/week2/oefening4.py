leeftijd_hond = int(input("Hoe oud is uw hond: "))

if leeftijd_hond <0:
    print("geef geldige leeftijd")
    
elif leeftijd_hond == 0:
    print("het is een puppy")

elif leeftijd_hond == 1:
    print("de leeftijd komt overeen met 14 mensenjaren")

elif leeftijd_hond == 2:
    print("de leeftijd komt overeen met 28 mensenjaren")

else:
    temp_leeftijd = 22 + (leeftijd_hond -2 ) * 5
    print(f"de leeftijd komt overeen met {temp_leeftijd} mensenjaren")