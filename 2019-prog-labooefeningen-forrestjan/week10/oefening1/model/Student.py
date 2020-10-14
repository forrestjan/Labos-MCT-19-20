from .Persoon import Persoon


class Student(Persoon):

    def __init__(self, parnaam, parvoornaam, parstudentennummer, paropleiding, pargeboortejaar=2019):
        # Persoon.__init__(self, parnaam, parvoornaam, pargeboortejaar)
        super().__init__(parnaam, parvoornaam, pargeboortejaar)
        self.studentennummer = parstudentennummer
        self.opleiding = paropleiding

    @property
    def studentennummer(self):
        return self._studentennummer

    @studentennummer.setter
    def studentennummer(self, value):
        if type(value) is int:
            self._studentennummer = value
        else:
            raise ValueError("Geen geldig studentennummer!")

    @property
    def opleiding(self):
        return self._opleiding

    @opleiding.setter
    def opleiding(self, value):
        if value:
            self._opleiding = value
        else:
            raise ValueError("Geen geldige opleiding!")

    def __str__(self):
        return f"Student {super().__str__()}"

    def __repr__(self):
        return f"{super().__str__()}"

    def __eq__(self, other):
        print("eq - Student")
        if self.studentennummer == other.studentennummer:
            return True
        else:
            return False
