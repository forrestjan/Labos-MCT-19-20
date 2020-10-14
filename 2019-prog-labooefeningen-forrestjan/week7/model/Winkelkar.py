class Winkelkar:
    #  Constructor ( _init_methode)
    def __init__(self):
        # voor producten is er geen SETTER property
        # rechtstreeks wegschrijven in het attribuut(een lege list)
        self._producten = []
    # properties (of eigenschappen)
    @property
    def producten(self):
        """The producten property."""
        return self._producten

    # --------------------------------------

    # --------------------------------------

    # --------------------------------------

    # --------------------------------------

    # to string methode (_str_)
    def __str__(self):
        aantal = len(self.producten)
        return f"de winkelkar bestaat uit{aantal}, {self.producten}"
    # extra methode

    def voeg_product_toe(self, parnaam_nieuw_product):
        self._producten.append(parnaam_nieuw_product)

    def verwijder_product(self, parnaam_bestaand_product):
        if parnaam_bestaand_product in self._producten:
            self._producten.remove(parnaam_bestaand_product)

    def __add__(self, other):
        w = Winkelkar()
        w._producten = self._producten + other.producten
        return w

    def __iadd__(self, other):
        w = Winkelkar()
        w._producten = self._producten + other.producten + ["geurkaarske"]
        return w
