class Voertuig():
    _aantal_voertuigen = 0

    def __init__(self, parid, parmerk, parbouwjaar, parkmstand):
        self._id = parid
        self._merk = parmerk
        self._bouwjaar = parbouwjaar
        self.kmstand = parkmstand
        self.reisbestemming = ""
        Voertuig._aantal_voertuigen += 1

    @property
    def id(self):

        return self._id

    @property
    def merk(self):
        return self._merk.upper()

    @property
    def bouwjaar(self):
        return self._bouwjaar

    @property
    def kmstand(self):
        return self._kmstand

    @kmstand.setter
    def kmstand(self, value):
        if type(value) is float or type(value) is int:
            self._kmstand = value
        else:
            raise ValueError("Geen geldige kmstand.")

    @property
    def reisbestemming(self):
        return self._reisbestemming

    @reisbestemming.setter
    def reisbestemming(self, value):
        if type(value) is str:
            self._reisbestemming = value
        else:
            raise ValueError("Geen geldige reisbestemming.")

    def __del__(self):
        Voertuig._aantal_voertuigen -= 1

    def __str__(self):
        return f"{self.merk} {self.bouwjaar}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.id == other.id:
            return True
        else:
            return False

    @staticmethod
    def geef_aantal_voertuigen():
        return Voertuig._aantal_voertuigen