class Bier:
    #  Constructor ( _init_methode)

    def __init__(self, parnaam, parbrouwerij, paralcoholpercentage, parkleur):
        self.naam = parnaam
        self.brouwerij = parbrouwerij
        self.alcoholpercentage = paralcoholpercentage
        self.kleur = parkleur
    # properties (of eigenschappen)
    @property
    def naam(self):
        """The naam property."""
        return self._naam.upper()

    @naam.setter
    def naam(self, value):
        if value != "":
            self._naam = value
        else:
            self._naam = "onbekend"
    # --------------------------------------
    @property
    def brouwerij(self):
        """The brouwerij property."""
        return self._brouwerij

    @brouwerij.setter
    def brouwerij(self, value):
        if value != "":
            self._brouwerij = value
        else:
            self._brouwerij = "onbekend"
    # --------------------------------------
    @property
    def alcoholpercentage(self):
        """The alcoholpercentage property."""
        return self._alcoholpercentage

    @alcoholpercentage.setter
    def alcoholpercentage(self, value):
        # controleer of het een kommagetal is
        if type(value) is float:
            self._alcoholpercentage = value
        else:
            self._alcoholpercentage = -1
    # --------------------------------------
    @property
    def kleur(self):
        """The kleur property."""
        return self._kleur

    @kleur.setter
    def kleur(self, value):
        if value != "":
            self._kleur = value
        else:
            self._kleur = "onbekend"
    # --------------------------------------
    # to string methode (_str_)

    def __str__(self):
        return f"{self.naam} {self.brouwerij} - {self.alcoholpercentage}"
