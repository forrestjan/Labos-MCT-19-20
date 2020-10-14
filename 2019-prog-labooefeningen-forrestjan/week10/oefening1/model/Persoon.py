from datetime import datetime


class Persoon:
    # klasse-attributen
    vereniging = "Howest"
    _aantal_personen = 0  # private!

    def __init__(self, parnaam, parvoornaam, pargeboortejaar=2016):
        self.naam = parnaam
        self.voornaam = parvoornaam
        self.geboortejaar = pargeboortejaar
        Persoon._aantal_personen += 1

    def __del__(self):
        Persoon._aantal_personen -= 1

    @property
    def naam(self):
        return self._naam

    @naam.setter
    def naam(self, value):
        if value != "":
            self._naam = value
        else:
            raise ValueError("Geen geldige naam")

    @property
    def voornaam(self):
        return self._voornaam

    @voornaam.setter
    def voornaam(self, value):
        if value != "":
            self._voornaam = value
        else:
            raise ValueError("Geen geldige voornaam")

    @property
    def geboortejaar(self):
        return self._geboortejaar

    @geboortejaar.setter
    def geboortejaar(self, value):
        # controle of de nieuwe waarde wel degelijk een int is
        if type(value) is int and value >= 1900 and value <= datetime.now().year:
            self._geboortejaar = value
        else:
            raise ValueError("Geen geldig geboortejaar")

    # extra property-methode(s)
    @property
    def leeftijd(self):
        verschil = datetime.now().year - self.geboortejaar
        return verschil

    def __str__(self):
        return f"{self.naam.upper()} {self.voornaam} ({self.geboortejaar})"

    def __repr__(self):
        return f"{self.naam.upper()} {self.voornaam}"

    def __eq__(self, other):
        print("eq - Persoon")
        if (self.naam == other.naam) and (self.voornaam == other.voornaam) and (
                self.geboortejaar == other.geboortejaar):
            return True
        else:
            return False

    # operator <    -> nodig als we list van objecten van de klasse Persoon willen sorteren
    def __lt__(self, other):
        # eerst proberen te sorteren op naam. Indien gelijke namen wordt de voornaam gebruikt
        if self.naam != other.naam:
            return self.naam < other.naam
        else:
            return self.voornaam < other.voornaam

    @staticmethod
    def geef_aantal_personen():
        return Persoon._aantal_personen
