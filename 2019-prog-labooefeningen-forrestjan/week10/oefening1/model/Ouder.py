from .Persoon import Persoon
from .Student import Student


class Ouder(Persoon):
    # Constructor ( _init_methode)
    def __init__(self, parnaam, parvoornaam, pargeboortejaar=2016):
        # self is: dit is een eigen klasse dat naar zigzelf verwijzed
        # bij static verwijs je naar aal de objecten
        # --------------------------------------
        # ik spreek dat constructor van de parent class aan(die zal ervoor zorgen)
        # dat de parameters in de atributen worden opgeslagen
        super().__init__(parnaam, parvoornaam, pargeboortejaar)
        # alternatief > Persoon.__init__(self,parnaam, parvoornaam, pargeboortejaar)
        self._studenten = []

    # properties (of eigenschappen)
    @property
    def studenten(self):
        """The studenten property."""
        return self._studenten
    # --------------------------------------
    # --------------------------------------
    # --------------------------------------
    # --------------------------------------

    # to string methode (_str_)
    # extra methode
    def voeg_student_toe(self, nieuwe_student):
        # controleer eerst of het type een student is
        # controleer of de student er nog niet inzit
        #  pas dan toevoegen
        # zoniet -> value error
        if type(nieuwe_student) is Student:
            # if type is nieuwe_student:
            if nieuwe_student not in self.studenten:
                self.studenten.append(nieuwe_student)
            else:
                raise ValueError("student zit al in de lijst studenten")

        else:
            raise ValueError("niet van het type student")
        # --------------------------------------

    def __str__(self):
        return f"ouder: {super().__str__()} met{len(self.studenten)}studenten"

    def __repr(self):
        return f"ouder: {super().__str__()}"

    def geef_info_studenten(self):
        resultaat = ""
        for student_item in self.studenten:
            resultaat += f"-{student_item} volgt de opleiding:{student_item.opleiding}\n"
        return resultaat

    def geef_opleidingen_studenten(self):
        resultaat_opl_studenten = []
        # overloop de kinderen van dit object. kijk of de opleiding in resultaat list zit
        # voeg het toe
        # return het
        for student_item in self.studenten:
            if student_item.opleiding not in resultaat_opl_studenten:
                resultaat_opl_studenten.append(student_item.opleiding)
        return resultaat_opl_studenten
