
import json
from .ProductColor import ProductColor


class MakeUpProduct:

    def __init__(self, parid, parbrand, parname, parprice, parproductlink):
        self.id = parid
        self.brand = parbrand
        self.name = parname
        self.price = parprice
        self.productlink = parproductlink
        self._colors = []

    @property
    def id(self):
        """The id property."""
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def brand(self):
        """The brand property."""
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def name(self):
        """The name property."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def productlink(self):
        """The productlink property."""
        return self._productlink

    @productlink.setter
    def productlink(self, value):
        self._productlink = value

    @property
    def price(self):
        """The price property."""
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def colors(self):
        """The colors property."""
        return self._colors

    def __str__(self):
        return f"{self.name} ({self.brand}) -> Available Colors: {len(self.colors)}"

    def __repr__(self):
        return f"{self.name}"

    def __lt__(self, other):
        if len(self.colors) < len(other.colors):
            return True
        else:
            return False

    def add_productcolor(self, new_color):
        if type(new_color) is ProductColor and new_color not in self._colors:
            self._colors.append(new_color)
        else:
            raise ValueError("Geen geldige kleur of kleur was al toegevoegd")
