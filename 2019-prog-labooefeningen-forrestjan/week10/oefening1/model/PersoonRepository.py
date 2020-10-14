import json
from .Student import Student
from .Ouder import Ouder


class PersoonRepository:
    # waar staat de json file?
    _filename = 'week10/doc/personen.json'
    # _ (private) = is enkel bruikbaar in deze klasse
    @staticmethod
    def _read_local_json_file(bestandsnaam):
        fo = open(bestandsnaam, encoding="utf8")
        response_json = fo.read()
        fo.close()
        return json.loads(response_json)

    @staticmethod
    def inlezen_ouders_met_studenten():
        list_met_ouders = []
        list_json = PersoonRepository._read_local_json_file(
            PersoonRepository._filename)
        for dict.item in list_json:

            # overloop de dict ouders in de json```
            # maak ouders aan, maak studenten aan
            # voeg studenten toe aan ouder
            # voeg de ouder  toe list_met_ouders
            # return uiteindelijk list met ouders
