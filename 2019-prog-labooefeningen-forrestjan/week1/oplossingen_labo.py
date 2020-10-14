# demo 
# print("hello world")

# # Oef 1
# print("Beel")
# print("Robbe")
# print("robbebeel2001@gmail.com")

# # Oef 1.2
# print("Beel\nRobbe\nrobbebeel2001@gmail.com")

# # Oef 2
# print("Labo basic prog \n\tlabo week 1\n\t\tKennismaking\n\t\tWerken met tabs")
# # \n toevoehing in dezelfde print 
# \t tab zorgt voor een spaciering, als je ze meermaals zet achter elkaar dan dan is de ruimte groter
# \\ 2 backslashes achter elkaar heeft een printable backslash
# \' plaatst een quotering die printable is zoder invloed op code 
# \" plaatst een dubbele quotering die printable is

#Oef3
### notes:  strings -> leterlijke tekst
###         int(eger)-> geheel getal
###         float    -> komma getal
###         als je nummers wil veranderen naar letters gebruik str( variable )
###         als je letters wil veranderen naar nummers gebruik int( variable )
##stap 1 - vraag aan de gebruiker
# naam = input ("geef een naam")
# voornaam = input ("geef een voornaam")
# leeftijd = int(input ("geef een leeftijd")) #dit is geen string maar een int
# ##stap 2 - Maak berekeningen 
# geboortejaar = 2019 - leeftijd
# ##stap 3 - toon de uitkomst
# print("welkom " + naam + " - " + voornaam + ": geb" + str(geboortejaar))

#Oef 4 berekenoppervlakte van een driehoek

### notes: belangerijk aan een variable: waarde, naam, en inhoud(tekst;kommagetal)
###        denk zoals een doosje en de inhoud is wat in het doosje zit
#basis = float(input("geef de basis van de driehoek op: "))
#print(basis)              #<--------- even kijken wat er in de variable zit
#print(type(basis))        #<--------- even kijken wat het datatype is 
#hoogte = float(input("geef de hoogte van de driehoek op: "))
#opp = basis * hoogte /2
#print(f"de oppervlakte van de driehoek bedraagt {opp}")

#oef 5
# dagen = int(input("Geef het aantal dagen op "))
# uren = int(input("Geef het aantal uren op "))
# minuten = int(input ("Geef het aantal minuten op "))
# seconden = int(input ("Geef het aantal seconden op "))

# totaal = seconden + minuten * 60 + uren *60 * 60 + dagen *24 *60 *60

# print(f"Het aantal seconde bedraagt{totaal}")

#oef 6
totaal_seconde = int(input("Geef het aantal seconde op "))

#hoeveel dagen/uren/minuten/seconde zitten hierin

aantal_sec_1dag = 24 * 60 * 60
#we voeren een gehele deling uit: uit resultaaat is dan een niet-komma getal
aantal_dagen = totaal_seconde //aantal_sec_1dag
print(aantal_dagen)

#de rest van een delen kan je via de modulo-operator dit is het ´%'
rest_seconde = totaal_seconde % aantal_sec_1dag
#stap 2: bereken hoeveel volle uren in de rest zitten
aantal_sec_in_1uur = 60 *60
aantal_uren = rest_seconde // aantal_sec_in_1uur
print(aantal_uren)
rest_seconde = rest_seconde % aantal_sec_in_1uur

#stap 3 hoeveel volle mintuen zitten er in de rest
aantal_sec_1mintuut = 60
aantal_minuten = rest_seconde // aantal_sec_1mintuut
print(aantal_minuten)
rest_seconde = rest_seconde % aantal_sec_1mintuut

print(f"{aantal_dagen}:{aantal_uren}:{aantal_minuten}:{rest_seconde}")

# Oef 7
cijfer = int(input("geef een cijfer op: "))

# 3 ---> 3 + 33 + 333
resultaat = cijfer + (cijfer * 11) + (cijfer * 111)
print(f"het resultaat is {resultaat}")

#oef 8
#vraag 2 getallen op
getal1 = int(input(geef het eerste getal op: ))
getal1 = int(input(geef het tweede getal op: ))

#doe de berekening 
resultaat = (getal1 + getal2) * (getal1 + getal2)

#print het resultaat
print(f"het resultaat is{resultaat}")

#oef 9
