from .Hotelgast import Hotelgast


class Hotel:
    #Constructor ( _init_methode)
    def __init__(self, par_hotel_naam):

        self.hotel_naam = par_hotel_naam
        # self._hotel_naam = par_hotel_naam
        # Pas op ^ vorig regel maakt geen gebruik van de property maar gaat rechtstreeks het attribut instellen
        # gebruik command/ control click om te zien wat hij doet
        self._gasten = []
        pass
    # properties (of eigenschappen)s
    @property
    def hotel_naam(self):
        """The hotel_naam property."""
        return self._hotel_naam

    @hotel_naam.setter
    def hotel_naam(self, value):
        if type(value) is str and value != "":
            self._hotel_naam = value
        else:
            self._hotel_naam = "smokinrocker"
    # --------------------------------------
    @property
    def gasten(self):
        """The gasten property."""
        return self._gasten
    # geen setter = private
    # --------------------------------------
    # --------------------------------------
    # --------------------------------------

    # to string methode (_str_)
    def __str__(self):
        return f"hotel: {self.hotel_naam}"
    # extra methode

    def check_in(self, naam, voornaam):
        nieuwe_gast = Hotelgast(naam, voornaam)
        return (f"{nieuwe_gast.ingecheked}:{nieuwe_gast} -- {paropen_saldo}")

    def _zoek_hotelgast(self, naam, voornaam):
        temp_gast = Hotelgast(naam, voornaam)

    def check_out(self, naam, voornaam):
        gast = self._zoek_hotelgast(naam, voornaam)
        if gast is not none:
            if gast.saldo > 0:
                print(f"")
            else:
                gast.is_ingechecked = False
                self.gasten.remove(gast)
                print(f"")
