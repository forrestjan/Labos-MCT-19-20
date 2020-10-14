import math


class Meetwiel:
    #  Constructor ( _init_methode)
    def __init__(self, parstraal=0, paromwenteling=0):
        self.straal = parstraal
        self.omwenteling = paromwenteling
    # properties (of eigenschappen)
    @property
    def straal(self):
        """The straal property."""
        return self._straal

    @straal.setter
    def straal(self, value):
        self._straal = value
    # --------------------------------------
    @property
    def omwenteling(self):
        """The omwenteling property."""
        return self._omwenteling

    @omwenteling.setter
    def omwenteling(self, value):
        self._omwenteling = value
    # --------------------------------------
    @property
    def omtrek(self):
        """The omtrek property."""
        # een property kan ook een berekening zijn op basis
        # van andere properties
        resultaat = 2 * self.straal * math.pi
        return resultaat
    # --------------------------------------

    def afstand(self):
        # een property kan ook een berekening zijn op basis
        # van andere properties
        resultaat = self.omtrek * self.omwenteling
        return resultaat
    # --------------------------------------

    # to string methode (_str_)
    def __str__(self):
        return f"straal :{self.straal} en omwenteling {self.omwenteling}"
