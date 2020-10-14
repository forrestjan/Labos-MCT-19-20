from.Geboortedatum import Geboortedatum


class Speler:
    naam_ploeg = ""
    _doelpunten_ploeg = 0

    def __init__(self, par_naam, par_voornaam, par_type, par_waarde=0, par_aantal_doelpunten=0, par_geboortedatum=Geboortedatum(1, 1, 2019)):
        self.naam = par_naam
        self.voornaam = par_voornaam
        self.type = par_type
        self.waarde = par_waarde
        self.geboortedatum = par_geboortedatum
        self._aantal_doelpunten = par_aantal_doelpunten
        Speler._doelpunten_ploeg += par_aantal_doelpunten

    # properties (of eigenschappen)
    @property
    def naam(self):
        """The naam property."""
        return self._naam

    @naam.setter
    def naam(self, value):
        self._naam = value
    # --------------------------------------
    @property
    def voornaam(self):
        """The voornaam property."""
        return self._voornaam

    @voornaam.setter
    def voornaam(self, value):
        self._voornaam = value
    # --------------------------------------
    @property
    def type(self):
        """The type property."""
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    # --------------------------------------
    @property
    def type(self):
        """The type property."""
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    # --------------------------------------
    @property
    def waarde(self):
        """The waarde property."""
        return self._waarde

    @waarde.setter
    def waarde(self, value):
        self._waarde = value
    # --------------------------------------
    @property
    def aantal_doelpunten(self):
        """The aantal_doelpunten property."""
        return self._aantal_doelpunten

    def maak_doelpunt(self):
        self._aantal_doelpunten += 1
        Speler._doelpunten_ploeg += 1
    # --------------------------------------
    @property
    def geboortedatum(self):
        """The geboortedatum property."""
        return self._geboortedatum

    @geboortedatum.setter
    def geboortedatum(self, value):
        if type(value) is Geboortedatum:
            self._geboortedatum = value
        else:
            self._geboortedatum = Geboortedatum(1, 1, 2019)
    # --------------------------------------
    @staticmethod  # static method werkt op zijn eigen
    def get_doelpunten_saldo_ploeg():
        return Speler._doelpunten_ploeg

    # to string methode

    def __str__(self):
        return f"{self.naam}, {self.voornaam} ({self.waarde}/10) doelpunten: {self.aantal_doelpunten}"
