import json

#Neem deze code NIET over. Dit is enkel om de structuur van de json-file te verkennen en te testen.

def _read_local_json_file(bestandsnaam):
    fo = open(bestandsnaam, encoding="utf8")
    response_json = fo.read()
    fo.close()
    return json.loads(response_json)

def test_bieren():
    list_json = _read_local_json_file("doc/bieren.json")      #je krijgt een dict terug
    #list van dictionaries
    for dict_element in list_json:
        print(f"Nummer: {dict_element['Nr']}")
        print(f"Naam: {dict_element['Naam']}")
        print(f"Brouwerij: {dict_element['Brouwerij']}")
        print(f"Kleur: {dict_element['Kleur']}")
        input("druk op enter voor volgende bier...")          


def test_makeup():
    list_json = _read_local_json_file("doc/makeupproducts.json")      #je krijgt een dict terug
    #list van dictionaries
    for dict_element in list_json:
        print(f"Id: {dict_element['id']}")
        print(f"Merk: {dict_element['brand']}")
        print(f"Naam: {dict_element['name']}")
        print(f"Prijs: {dict_element['price']}")
        print(f"Link: {dict_element['product_link']}")

        #kleuren opvragen: list van dictionaries
        list_kleuren = dict_element["product_colors"]
        print("Beschikbare kleuren:")
        for dict_kleur in list_kleuren:
            print(f"\t- {dict_kleur['colour_name']}")      
        input("druk op enter voor volgende product...")      

# test_bieren()
test_makeup()