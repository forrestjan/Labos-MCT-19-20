#Vraag aan de gebruiker wat zijn geboortejaar is. Indien hij nog geen 18 is, print dan ook een gepaste melding af.
from datetime import datetime
#je importeert een "boek" datetime uit de bibliotheek datetime
geboortejaar = int(input("geef uw geboortejaar op: "))

vandaag = datetime.now()

ouderdom = vandaag.year - geboortejaar

if ouderdom >= 18:
    print(f"ok u mag alcohol drinken {ouderdom}")
else:
    print(f" u bent nog geen 18 maar {ouderdom} \nKom volgend jaar terug")