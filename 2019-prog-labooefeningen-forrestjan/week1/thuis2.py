#Schrijf een programma dat een kassasysteem nabootst.
# Een broek kost 70,5 euro.
# Een T-shirt kost 20,89 euro.
# Een vest kost 100,3 euro.
# De gebruiker geeft per item het aantal gekochte goederen in. De computer berekent het te betalen bedrag.
aantal_broek = float(input("geef aankoop aantal broeken "))
aantal_tshirt = float(input("geef aankoop aantal tshirts "))
aantal_vest = float(input("geef aankoop aantal vesten "))

prijs_broek = 70.5
prijs_tshirt =  20.89
prijs_vest = 100.3

totaal_broek = aantal_broek * prijs_broek
totaal_tshirt = aantal_tshirt * prijs_tshirt
totaal_vest = aantal_vest * prijs_vest

alles_samen = totaal_broek + totaal_tshirt + totaal_vest

print(f"*** welkom bij het kassasysteem ***\nHoeveel broeken werden er gekocht? {aantal_broek} \nHoeveel tshirts werden er gekocht? {aantal_tshirt}\nHoeveel vesten werden er gekocht? {aantal_vest}\nTotaal te betallen:{alles_samen}")