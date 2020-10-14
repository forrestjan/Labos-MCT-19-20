#Oef 4 berekenoppervlakte van een driehoek

### notes: belangerijk aan een variable: waarde, naam, en inhoud(tekst;kommagetal)
###        denk zoals een doosje en de inhoud is wat in het doosje zit
basis = float(input("geef de basis van de driehoek op: "))
print(basis)              #<--------- even kijken wat er in de variable zit
print(type(basis))        #<--------- even kijken wat het datatype is 
hoogte = float(input("geef de hoogte van de driehoek op: "))
opp = basis * hoogte /2 #<----- 1 / betekent een deling met komma getallen Bij 2 // zal er geen kommagetal vertoont worden bij de output (terminal)
print(f"de oppervlakte van de driehoek bedraagt {opp}")

