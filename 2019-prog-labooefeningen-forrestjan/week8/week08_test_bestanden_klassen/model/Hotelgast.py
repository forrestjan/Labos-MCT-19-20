class Hotelgast:
    #Constructor ( _init_methode)
    def __init__(self, parnaam, parvoornaam, paropen_saldo, paringecheked):
        self.naam = parnaam
        self.voornaam = parvoornaam
        self.open_saldo = paropen_saldo
        self.ingecheked = paringecheked
    # properties (of eigenschappen)s
    @property
    def naam(self):
        """The naam property."""
        return self._naam

    @naam.setter
    def naam(self, value):
        if naam != "":
            self._naam = value
        else:
            self._naam = "ONBEKEND"
    # --------------------------------------
    @property
    def voornaam(self):
        """The voornaam property."""
        return self._voornaam

    @voornaam.setter
    def voornaam(self, value):
        if voornaam != "":
            self._voornaam = value
        else:
            self._voornaam = "ONBEKEND"
    # --------------------------------------
    @property
    def open_saldo(self):
        """The open_saldo property."""
        return self._open_saldo

    @open_saldo.setter
    def open_saldo(self, value):
        if type is int and value > 0:
            self._open_saldo = value
        else:
            self.open_saldo = 0
    # --------------------------------------

    @property
    def ingecheked(self):
        """The ingecheked property."""
        return self._ingecheked

    @ingecheked.setter
    def ingecheked(self, value):
        if type(value) is bool:
            self._ingecheked = value
        else:
            self._ingecheked = False
    # to string methode (_str_)

    def __str__(self):
        if self.ingecheked == True:
            return f"ok: {self.naam} - {self.saldo}"
        else:
            return f"X: {self.voornaam} {self.naam}"

    # extra methode
    def __eq__(self, other):
        if self.naam and self.voornaam == other.naam and other.voornaam:
            return True
        else:
            return False

    def __repr__(self):
        # lijst hotelgasten weergeven
        return self.__str__()
