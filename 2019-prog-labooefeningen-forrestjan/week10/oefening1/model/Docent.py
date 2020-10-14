from .Persoon import Persoon


class Docent(Persoon):
    def __init__(self, parnaam, parvoornaam, parpersoneelsnummer, pargeboortejaar=2016):
        super().__init__(parnaam, parvoornaam, pargeboortejaar)
        self.personeelsnummer = parpersoneelsnummer
        self._opleidingen = []  # list: in welke opleidingen geeft hij/zij les?

    @property
    def personeelsnummer(self):
        return self._personeelsnummer

    @personeelsnummer.setter
    def personeelsnummer(self, value):
        if type(value) is int:
            self._personeelsnummer = value
        else:
            raise ValueError("Geen geldig personeelsnummer!")

    @property
    def opleidingen(self):
        return self._opleidingen

    def geeft_les_in(self, opleiding):
        if opleiding not in self.opleidingen:
            self._opleidingen.append(opleiding)

    def __str__(self):
        return "Docent " + super().__str__()

    def __eq__(self, other):
        print("eq - Docent")
        if (self.personeelsnummer == other.personeelsnummer):
            return True
        else:
            return False
