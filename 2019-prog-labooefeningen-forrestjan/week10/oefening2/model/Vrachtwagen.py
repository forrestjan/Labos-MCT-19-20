from model.Voertuig import Voertuig


class Vrachtwagen:
    # Constructor ( _init_methode) <- hier zet je atributten
    def __init__(self, parvracht, parmax_laadvermogen, parid, parmerk, parbouwjaar, parkmstand):
        self.vracht = 0
        self.max_laadvermogen = parmax_laadvermogen

        self._id = parid
        self._merk = parmerk
        self._bouwjaar = parbouwjaar
        self.kmstand = parkmstand
    # properties (of eigenschappen)
    # self.property = public attribute
    # self._property = protected attribute
    # self.__property = Private attribute

    @property
    def vracht(self):
        """The vracht property."""
        return self._vracht

    @vracht.setter
    def vracht(self, value):
        if type(value) is float and value <= self.max_laadvermogen:
            self._vracht = value
        else:
            raise ValueError("te zware vracht")
    # --------------------------------------
    @property
    def max_laadvermogen(self):
        """The max_laadvermogen property."""
        return self._max_laadvermogen

    @max_laadvermogen.setter
    def max_laadvermogen(self, value):
        if type(value) is float:
            self._max_laadvermogen = value
        else:
            raise ValueError("foutieve waarde voor laadvermogen")

    # --------------------------------------
    # --------------------------------------
    # --------------------------------------
    # to string methode (_str_)
    # extra methode
