
#prijs_tshirt =  20.89
#prijs_vest = 100.3


def broek_totaal(broek_aantal, broek_prijs=70.5):
    return (broek_aantal * broek_prijs)

aantal_broeken = int(input("geef uw aantal broeken op :"))

print(f"uw totaal bedrag bedraagt {broek_totaal(aantal_broeken)}")
