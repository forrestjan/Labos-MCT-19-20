#import json niet vergeten !!!
import json
from .Bier import Bier

class BierRepository:
    # waar staat de json file?
    _filename = 'doc/bieren.json'

    # _ (private) = enkel bruikbaar in deze klasse
    @staticmethod
    def _read_local_json_file(bestandsnaam):
        fo = open(bestandsnaam, encoding="utf8")
        response_json = fo.read()
        fo.close()
        return json.loads(response_json)

    @staticmethod
    def inlezen_bieren():
        # lees alle info uit json = list
        #overloop deze list, elk element is een dict
        #van elk element maak je een klasse Bier
        # voeg dit object toe aan list
        # Return deze list
        list_resultaat= []
        list_json = BierRepository._read_local_json_file(BierRepository._filename)
        for dict_bier_element in list_json:
            try:
                temp_naam = dict_bier_element["Naam"]
                temp_brouwerij = dict_bier_element["Brouwerij"]
                temp_kleur = dict_bier_element["Kleur"]
                temp_alcohol = float(dict_bier_element["alcohol"])

                temp_bierke = Bier(temp_naam, temp_brouwerij,temp_alcohol, temp_kleur)

                list_resultaat.append(temp_bierke)
            except Exception as ex:
                print(f"Fout bij inlezen bier {ex}")

        return list_resultaat
        
    @staticmethod
    def zoek_bieren_uit_brouwerij(list_bieren, zoekterm):
        resultaat = []
        # overloop items van type bier uit list
        for bier_item in list_bieren:
        # haal de brouwerij op uit dit item en als de zoekterm er in staat, voeg toe aan nieuwe list resultaat
            if zoekterm.lower() in bier_item.brouwerij.lower():
                resultaat.append(bier_item)
        return resultaat