from .Persoon import Persoon


class Auto:
    def __init__(self, parnummerplaat, pareigenaar):
        # prop gebruiken ipv attribuut
        self.nummerplaat = parnummerplaat
        self.eigenaar = pareigenaar

    @property
    def nummerplaat(self):
        return self._nummerplaat

    @nummerplaat.setter
    def nummerplaat(self, value):
        self._nummerplaat = value

    @property
    def eigenaar(self):
        return self._eigenaar

    @eigenaar.setter
    def eigenaar(self, value):
        # if type(value) is persoon:
        # isistance doet het zelfde als type()is
        # maar controleert ook of het object een child is van een bepaalde klasse
        # NUTTIG BIJ ERVEN
        if isinstance(value) is Persoon:
            self._eigenaar = value
        else:
            raise ValueError("Geen object van de klasse Persoon")

    def __str__(self):
        # prop gebruiken ipv attribuut
        return f"Voertuig met kenteken {self.nummerplaat} heeft als eigenaar: {self.eigenaar}"
