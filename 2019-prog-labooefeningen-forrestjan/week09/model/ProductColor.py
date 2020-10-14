class ProductColor:

    def __init__(self, parcolorname, parhexvalue):
        self.colorname = parcolorname
        self.hexvalue = parhexvalue

    @property
    def hexvalue(self):
        """The hexvalue property."""
        return self._hexvalue

    @hexvalue.setter
    def hexvalue(self, value):
        self._hexvalue = value

    @property
    def colorname(self):
        """The colorname property."""
        return self._colorname

    @colorname.setter
    def colorname(self, value):
        self._colorname = value

    def __str__(self):
        return f"{self.colorname}"

    def __repr__(self):
        return f"{self.colorname}"

    def __eq__(self, other):
        if self.colorname == other.colorname and self.hexvalue == other.hexvalue:
            return True
        else:
            return False
