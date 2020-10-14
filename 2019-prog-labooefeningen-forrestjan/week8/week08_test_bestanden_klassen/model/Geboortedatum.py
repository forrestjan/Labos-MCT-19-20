import random
from datetime import datetime


class Geboortedatum:
    _aantal_geboortedata = 0  # private static variable
    #  Constructor ( _init_methode)

    def __init__(self, par_dag, par_maand, par_jaar):
        self.dag = par_dag
        self.maand = par_maand
        self.jaar = par_jaar
        Geboortedatum._aantal_geboortedata += 1
    # properties (of eigenschappen)
    @property
    def dag(self):
        """The dag property."""
        return self._dag

    @dag.setter
    def dag(self, value):
        if type(value) is int:
            self._dag = value
        else:
            self._dag = -1  # error
    # --------------------------------------
    @property
    def maand(self):
        """The maand property."""
        return self._maand

    @maand.setter
    def maand(self, value):
        if type(value) is int:
            self._maand = value
        else:
            self.maand = -1  # error
    # --------------------------------------
    @property
    def jaar(self):
        """The jaar property."""
        return self._jaar

    @jaar.setter
    def jaar(self, value):
        if type(value) is int:
            self._jaar = value
        else:
            self.jaar = -1  # error
    # to string methode (_str_)

    def __str__(self):
        return f"{self._dag}/{self._maand}/{self._jaar}"

    def __eq__(self, other):
        if self.dag == other.dag and self.maand == other.maand and self.jaar == other.jaar:
            return True
        else:
            return False

    @staticmethod
    def geef_aantal_geboortedata():
        return Geboortedatum._aantal_geboortedata
        # extra methode

    @staticmethod
    def genereer_willekeurige_geboortedatum():
        jaar = random.randint(1900, datetime.now().year)
        maand = random.randint(1, 12)
        dag = random.randint(1, 31)
        if maand in [1, 3, 5, 7, 8, 10, 12]:
            dag = random.randint(1, 31)
        elif maand in [2]:
            dag = random.randint(1, 28)
        else:
            dag = random.randint(1, 30)

        geb_datum = Geboortedatum(dag, maand, jaar)
        return geb_datum

    @staticmethod
    def genereer_lijst_geboortedata(aantal):
        verjaardagen = []
        for index in range(0, aantal):
            verjaardagen.append(
                Geboortedatum.genereer_willekeurige_geboortedatum())
        return verjaardagen
