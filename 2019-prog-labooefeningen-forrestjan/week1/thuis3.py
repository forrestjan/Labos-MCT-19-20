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

print(f"*** welkom bij het kassasysteem ***\nHoeveel broeken werden er gekocht? {aantal_broek}\nHoeveel tshirts werden er gekocht? {aantal_tshirt}\nHoeveel vesten werden er gekocht?{aantal_vest}\nu kocht:\n\tbroeken:{aantal_broek} stuk(s)\n\ttshirts:{aantal_tshirt} stuk(s)\n\tvesten:{aantal_vest} stuk(s)\nTotaal te betallen:{alles_samen}")