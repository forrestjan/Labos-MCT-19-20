class Auto:
    #  Constructor ( _init_methode)
    def __init__(self, parmerk, parmodel, parkleur, parbrandstof):
        # als ik een auto aanmaak, is de km stand ALTIJD 0
        self.kmstand = 0
        self.kleur = parkleur
        # als er geen setter is, dan bewaar je het rechstreeks in  de atribute
        self._merk = parmerk
        self._model = parmodel
        self._brandstof = parbrandstof
    # properties (of eigenschappen)
    @property
    def merk(self):
        """The merk property."""
        return self._merk
    # --------------------------------------
    @property
    def model(self):
        """The model property."""
        return self._model
    # --------------------------------------
    @property
    def kleur(self):
        """The kleur property."""
        return self._kleur

    @kleur.setter
    def kleur(self, value):
        self._kleur = value
    # --------------------------------------
    @property
    def brandstof(self):
        """The brandstof property."""
        # return de brandstof altijd in lowercase
        return self._brandstof.lower()
    # --------------------------------------
    @property
    def kmstand(self):
        """The kmstand property."""
        return self._kmstand

    @kmstand.setter
    def kmstand(self, value):
        self._kmstand = value
    # to string methode (_str_)

    def __str__(self):
        return f"{self._merk} (model: {self._model} kleur:{self._kleur})"

    # extra methode
    def rijden(self, parextra_km):
        self.kmstand += parextra_km

    def maak_lawaai(self):
        if self.brandstof == "diesel":
            return "vroom vroom"
        elif self.brandstof == "benzine":
            return "skrrt skrrt"
        elif self.brandstof == "elektrisch":
            return "ssssstttttt"
        else:
            return "ge staat in panne"
