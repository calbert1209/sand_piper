
class RGBValue:
    def __init__(self, r: int, g: int, b: int) -> None:
        self._r = self.__clamp__(r)
        self._g = self.__clamp__(g)
        self._b = self.__clamp__(b)

    def __clamp__(self, value: int):
        return max(0, min(value, 255))

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value: int):
        self._r = self.__clamp__(value)

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value: int):
        self._g = self.__clamp__(value)

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value: int):
        self._b = self.__clamp__(value)

    @property
    def hexaDecimalString(self):
        return f"{self._r:02x}{self._g:02x}{self._b:02x}"

    @property
    def hexValue(self):
        return int(self.hexaDecimalString, 16)
