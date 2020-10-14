#Om de prijs van een woning te bepalen, telt men de prijs van de bouwgrond en de eigenlijke bouw op. Het btwtarief
##Je vraagt aan de gebruiker de prijs van de bouwgrond en de prijs van het gebouw.
#Je toont het totaal te betalen bedrag.

prijs_bouwgrond = int(input("geef de prijs van de bouwgrond "))
prijs_gebouw = int(input("Geef de prijs van het gebouw "))

totaal = prijs_bouwgrond + prijs_gebouw 
totaal_tax = totaal + (totaal / 100 * 21)

print(f"uw totaale kosten met tax zijn {totaal_tax}")