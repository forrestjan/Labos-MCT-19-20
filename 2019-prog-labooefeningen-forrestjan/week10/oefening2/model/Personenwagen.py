from model.Voertuig import Voertuig


class Personenwagen:
    # Constructor ( _init_methode) <- hier zet je atributten
    def __init__(self, par_max_aantal_zitplaats, par_aantal_pers):
        self.aantal_pers = par_aantal_pers
        self.max_aantal_zitplaats = par_max_aantal_zitplaats
    # self.property = public attribute
    # self._property = protected attribute
    # self.__property = Private attribute
    # properties (of eigenschappen)
    @property
    def max_aantal_zitplaats(self):
        """The max_aantal_zitplaats property."""
        return self._max_aantal_zitplaats

    @max_aantal_zitplaats.setter
    def max_aantal_zitplaats(self, value):
        if type(value) is int and value >= 0:
            self._max_aantal_zitplaats = value
        else:
            raise ValueError("fout ingegeven")
    # --------------------------------------
    @property
    def aantal_pers(self):
        """The aantal_pers property."""
        return self._aantal_pers

    @aantal_pers.setter
    def aantal_pers(self, value):
        if type(value) is int and value <= self.max_aantal_zitplaats:
            self._aantal_pers = value
        else:
            raise ValueError("fout ingegeven")

    # to string methode (_str_)
    # extra methode
