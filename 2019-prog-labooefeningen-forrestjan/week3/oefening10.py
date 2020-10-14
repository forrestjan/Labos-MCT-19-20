# aantal_producten = int(input("geef uw aantal producten op > "))
# while aantal_producten != 0:
#    if aantal_producten == 0:
#        print(f"{aantal_groenten} producten zitten in de categorie Groenten \nTotale kostprijs {totaal_kostgroenten}\nGemiddelde prijs per product #{gemidelde_kostgroenten}")
#        print(f"{aantal_fruit} producten zitten in de categorie Groenten \nTotale kostprijs {totaal_kostfruit}\nGemiddelde prijs per product #{gemidelde_kostfruit}")
#
#        print(f"{aantal_fruit} producten zitten in de categorie Groenten \nTotale kostprijs {totaal_kostfruit}\nGemiddelde prijs per product #{gemidelde_kostfruit}")
#    else:
#        categorie_product = input("Wat is de categorie? [G:Groente , F:Fruit , D:Drank]")
#
aantal_producten = int(input("hoeveel producten wens je in te geven > "))

aantal_groenten = 0
aantal_fruit = 0
aantal_drank = 0

prijs_groenten = 0
prijs_fruit = 0
prijs_drank = 0

for index in range(1, aantal_producten+1):
    categorie = input(
        "wat is de categorie? [G: Groente, F: Fruit, D:Drank] > ")

    if str.upper(categorie) == "G":
        kostprijs = float(input("Wat is de prijs van het product"))
        aantal_groenten += 1
        prijs_groenten += kostprijs

    elif str.upper(categorie) == "F":
        aantal_fruit += 1
        prijs_fruit += kostprijs
    elif str.upper(categorie) == "D":
        aantal_drank += 1
        prijs_drank += kostprijs

    else:
        print("dit is een ongeldige keuze")
# In deze oefening zullen er fouten optreden indienn geen producten in de categorie aanwezig zijn
print(f"Er zijn {aantal_groenten} producten in de categorie groenten")
print(
    f"de gemidelde prijs van de groenten is : {prijs_groenten/aantal_groenten:.2f}")

print(f"Er zijn {prijs_fruit} producten in de categorie groenten")
print(f"de gemidelde prijs van de groenten is: {prijs_fruit/aantal_fruit:.2}")

print(f"Er zijn {aantal_drank} producten in de categorie groenten")
print(f"de gemidelde prijs van de groenten is : {prijs_drank/prijs_drank:.2f}")
