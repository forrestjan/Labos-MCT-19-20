class Bier:

    def __init__(self, parnaam, parbrouwerij, paralcoholpercentage, parkleur):
        # hieronder maken we gebruik van de properties!
        self.naam = parnaam
        self.brouwerij = parbrouwerij
        self.alcoholpercentage = paralcoholpercentage
        self.kleur = parkleur

    @property
    def naam(self):
        return self._naam

    @naam.setter
    def naam(self, nieuwenaam):
        if (nieuwenaam != ""):
            self._naam = nieuwenaam.upper()
        else:
            # self._naam = "onbekend"
            raise ValueError("Geen geldige biernaam")

    @property
    def brouwerij(self):
        return self._brouwerij

    @brouwerij.setter
    def brouwerij(self, nieuwebrouwerij):
        if (nieuwebrouwerij != ""):
            self._brouwerij = nieuwebrouwerij
        else:
            # self._brouwerij = "onbekend"
            raise ValueError("Geen geldige brouwerijnaam, kan niet leeg zijn")

    @property
    def alcoholpercentage(self):
        return self._alcoholpercentage

    @alcoholpercentage.setter
    def alcoholpercentage(self, nieuwalcoholpercentage):
        if type(nieuwalcoholpercentage) is float \
                and (nieuwalcoholpercentage >= 0) \
                and (nieuwalcoholpercentage <= 100):
            self._alcoholpercentage = nieuwalcoholpercentage
        else:
            # self._alcoholpercentage = -1
            raise ValueError(
                "Geen geldig percentage, moet een float zijn tss 0 en 100")

    @property
    def kleur(self):
        return self._kleur

    @kleur.setter
    def kleur(self, nieuwkleur):
        if (nieuwkleur.strip() != ""):
            self._kleur = nieuwkleur
        else:
            # self._kleur = "onbekend"
            raise ValueError("Geen geldig kleur, mag niet leeg zijn")

    def __str__(self):
        return f"{self.naam} {self.brouwerij} - {self.alcoholpercentage}"

    def __repr__(self):
        return f"- {self.naam}\n"
