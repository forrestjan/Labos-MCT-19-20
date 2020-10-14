class Boek:
    #Constructor ( _init_methode)
    # parjaartaal is optioneel word het niet opgegeven dan krijgt het de waarde 2019
    # *****--------VOOR LIAM------------*****
    #   wees zeker dat je bij de def__init__() **self** hebt staan anders krijg je een error
    #   check dat bij init en str 2x een  _ staat === __init__ & __str__
    #   waneer je in de init de parameters meegeeft MOETEN ze in de chronologische volgorde
    #   de juiste Python snippet is van cstrap
    # *****----------------------------------*****
    def __init__(self, partitel, parauteur, paruitgeverij, parisbn, parjaargang=2019):
        self.titel = partitel
        self.auteur = parauteur
        self.uitgeverij = paruitgeverij
        self.isbn = parisbn
        self.jaargang = parjaargang
    # properties (of eigenschappen)s
    @property
    def titel(self):
        """The titel property."""
        return self._titel

    @titel.setter
    def titel(self, value):
        self._titel = value
    # --------------------------------------
    @property
    def auteur(self):
        """The auteur property."""
        return self._auteur

    @auteur.setter
    def auteur(self, value):
        self._auteur = value
    # --------------------------------------
    @property
    def uitgeverij(self):
        """The uitgeverij property."""
        return self._uitgeverij

    @uitgeverij.setter
    def uitgeverij(self, value):
        self._uitgeverij = value
    # --------------------------------------
    @property
    def isbn(self):
        """The isbn property."""
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        self._isbn = value
    # --------------------------------------
    @property
    def jaargang(self):
        """The jaargang property."""
        return self._jaargang

    @jaargang.setter
    def jaargang(self, value):
        self._jaargang = value
    # --------------------------------------
    # string methode (_str_)
    # toon nuttige info over het object
    # als het geprint word

    def __str__(self):
        return f"{self.auteur} , {self.titel} , ({self.uitgeverij}) ***{self.jaargang}***"
