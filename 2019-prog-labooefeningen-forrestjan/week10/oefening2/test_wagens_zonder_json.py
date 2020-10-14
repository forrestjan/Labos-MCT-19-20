from model.Personenwagen import Personenwagen
from model.Vrachtwagen import Vrachtwagen

rental1 = Personenwagen(100, "Audi", 2010, 3000, 5)
rental2 = Personenwagen(101, "Volkswagen", 2016, 0, 5)
rental3 = Vrachtwagen(102, "DAF", 2009, 3000, 5000)

list_met_rentals = [rental1, rental2, rental3]
print("*** Dit zijn de beschikbare voertuigen ****")
for item in list_met_rentals:
    print(item)

print("*** Geef de nieuwe bestemming van de voertuigen ****")
for item in list_met_rentals:
    temp_reisbestemming = input(f"Voor {item} > ")
    item.reisbestemming = temp_reisbestemming

print("*** Er stappen 3 personen in de Volkswagen ****")
list_met_rentals[1].aantal_personen = 3
print("*** De vrachtwagen wordt geladen ****")
try:
    temp_vracht = float(input(
        f"Hoeveel vracht neemt deze vrachtwagen mee? (max: {list_met_rentals[2].max_laadvermogen}) > "))
    list_met_rentals[2].vracht = temp_vracht
except Exception as ex:
    print(f"Foutje: {ex}")

print("*** toon details per rental car ****")
for item in list_met_rentals:
    print(item.geef_detail_info())
