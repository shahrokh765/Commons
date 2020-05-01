from Commons.Point import Point, CartesianPoint


class Element:

    def __init__(self, location: Point, height: float):
        self.__loc = location
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def location(self):
        return self.__loc

    @location.setter
    def location(self, location: float):
        self.__loc = location

    def __mul__(self, mul: int):
        return Element(self.location * mul, self.height)

    def __str__(self):
        return "location=({loc})\nheight={height}".format(loc=self.location, height=self.height)


class TX:

    def __init__(self, element: Element, power: float=-float('inf')):
        self.__elm = element
        self.__p = power  # power sent in dB

    @property
    def element(self):
        return self.__elm

    @element.setter
    def element(self, element: float):
        self.__elm = element

    @property
    def power(self):
        return self.__p

    @power.setter
    def power(self, power: float):
        self.__p = power

    def __str__(self):
        return "{elm}\npower={power}".format(elm=self.element, power=round(self.power, 3))


class RX:

    def __init__(self, element: Element):
        self.__elm = element
        self.__rp = -float('inf')  # received power in dB

    @property
    def element(self):
        return self.__elm

    @element.setter
    def element(self, element: float):
        self.__elm = element

    @property
    def received_power(self):
        return self.__rp

    @received_power.setter
    def received_power(self, received_power: float):
        self.__rp = received_power

    def __str__(self):
        return "{elm}\nreceived power={power}".format(elm=self.element, power=round(self.received_power,3))


if __name__ == "__main__":
    elm = Element(Point(CartesianPoint(5, 5)), 10)
    print(elm)
    print(elm.location)
    tx = TX(elm, -5)
    print(tx)
    print(tx.element.location)
    rx = RX(elm)
    print(rx)
    rx.received_power = -25.0
    print(rx)