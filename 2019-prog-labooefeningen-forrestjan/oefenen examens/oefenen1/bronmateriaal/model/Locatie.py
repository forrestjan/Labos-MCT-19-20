import logging


class Locatie:

    # straat, latitude (float!), longitude(float!)
    def __init__(self, parstraat, pargemeente, parlatitude, parlongitude):
        self.straat = parstraat
        self.latitude = parlatitude
        self.longitude = parlongitude
        self.gemeente = pargemeente

    @property
    def gemeente(self):
        return self._gemeente

    @gemeente.setter
    def gemeente(self, value):
        if isinstance(value, str) and value != "":
            self._gemeente = value
        else:
            raise ValueError("Ongeldige gemeentenaam")

    @property
    def straat(self):
        return self._straat

    @straat.setter
    def straat(self, value):
        if isinstance(value, str) and value != "":
            self._straat = value
        else:
            raise ValueError("Ongeldige straatnaam")

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if isinstance(value, float):
            self._latitude = value
        else:
            raise ValueError("Ongeldige latitude waarde")

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if isinstance(value, float):
            self._longitude = value
        else:
            raise ValueError("Ongeldige longitude waarde")

    def __str__(self):
        return f"{self.straat} te {self.gemeente}"

    def __repr__(self):
        return f"{self.straat} te {self.gemeente}"    


