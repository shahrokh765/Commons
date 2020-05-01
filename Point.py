import math
from collections import namedtuple
# from typing import NamedTuple

CartesianPoint = namedtuple('CartesianPoint', ('x', 'y'))
PolarPoint = namedtuple('PolarPoint', ('r', 'theta'))
GeographicPoint = namedtuple('GeographicPoint', ('lat', 'lon'))
# TODO move these two to commons


class Point:
    """Creating Point object. Argument of constructor can be one of CartesianPoint, PolarPoint, or a tuple.
    In case of tuple, it's assumed as a CartesianPoint"""
    def __init__(self, point):
        if isinstance(point, CartesianPoint):
            self.__cartesian = point
            self.__polar = self.__to_polar(point)
        elif isinstance(point, PolarPoint):
            self.__polar = point
            self.cartesian = self.__to_cartesian(point)
        elif isinstance(point, tuple) and len(point) == 2:
            self.__cartesian = CartesianPoint(point[0], point[1])
            self.__polar = self.__to_polar(self.__cartesian)
        # self.get_cartesian = self.get_cartesian()

    @staticmethod
    def __to_polar(cartesian_point: CartesianPoint) -> PolarPoint:
        x, y = cartesian_point.x, cartesian_point.y
        r = math.sqrt(x ** 2 + y ** 2)
        if x == 0:
            theta = math.atan(float('inf'))
        else:
            theta = math.atan(y / x)
        return PolarPoint(r, theta)

    @staticmethod
    def __to_cartesian(polar_point: PolarPoint) -> CartesianPoint:
        return CartesianPoint(polar_point.r * math.cos(polar_point.theta),
                              polar_point.r * math.sin(polar_point.theta))

    @property
    def cartesian(self) -> CartesianPoint:
        """Return cartesian information accessed by x and y"""
        return self.__cartesian

    @property
    def polar(self) -> PolarPoint:
        """Return polar information accessed by r and theta"""
        return self.__polar

    @polar.setter
    def polar(self, point: PolarPoint):
        self.__polar = point
        self.__cartesian = self.__to_cartesian(point)

    @cartesian.setter
    def cartesian(self, point: CartesianPoint):
        self.__cartesian = point
        self.__polar = self.__to_polar(point)

    def set(self, other: 'Point'):
        """Replace self with other"""
        self.__polar = other.polar
        self.__cartesian = other.cartesian

    def distance(self, other: 'Point') -> float:
        """Return distance between self and other"""
        return math.sqrt(pow(self.cartesian.x - other.cartesian.x, 2) + pow(self.cartesian.y - other.cartesian.y, 2))

    def add(self, other: 'Point') -> 'Point':
        """Return a new Point from adding two pints self and other.
        This does not set self with new values. To set use set functions."""
        return Point(CartesianPoint(self.cartesian.x + other.cartesian.x, self.cartesian.y + other.cartesian.y))

    def add_polar(self, other: PolarPoint) -> 'Point':
        """Return a new Point from adding self and a polar point.
        This does not set self with new values. To set use set functions."""
        return Point(CartesianPoint(self.cartesian.x + other.r * math.cos(other.theta),
                     self.cartesian.y + other.r * math.sin(other.theta)))

    def add_cartesian(self, other: CartesianPoint) -> 'Point':
        """Return a new Point from adding self and a cartesian point.
        This does not set self with new values. To set use set functions."""
        return Point(CartesianPoint(self.cartesian.x + other.x, self.cartesian.y + other.y))

    def __add__(self, other):
        """Return a new Point from adding two pints self and other.
        This does not set self with new values. To set use set functions."""
        return Point(CartesianPoint(self.cartesian.x + other.cartesian.x, self.cartesian.y + other.cartesian.y))

    def __sub__(self, other):
        """Return a new Point from adding two pints self and other.
        This does not set self with new values. To set use set functions."""
        return Point(CartesianPoint(self.cartesian.x - other.cartesian.x, self.cartesian.y - other.cartesian.y))

    def __mul__(self, mul: int):
        """Return a new Point from multiplication of self and an integer.
        This does not set self with new values. To set use set functions."""
        return Point(CartesianPoint(self.cartesian.x * mul, self.cartesian.y * mul))

    def __str__(self):
        return "{x},{y}".format(x=self.cartesian.x, y=self.cartesian.y)


def to_geographic(ref: GeographicPoint, point: Point) -> GeographicPoint:
    """ get location in (lat, lon) format when x and y is present"""
    offset = GeographicPoint(-1/111111, -1/111111)  # offset for one meter that should be added to upper_left_loc
    return GeographicPoint(ref.lat + point.cartesian.y * offset.lat, ref.lon + point.cartesian.x * offset.lon /
                           math.cos(math.radians(ref.lat + point.cartesian.y * offset.lat)))


if __name__ == "__main__":
    print(10*Point((1, 2)).distance(Point((1, 5))))
    print(Point((1, 3)))
    p = Point(CartesianPoint(0, 1))
    pp = Point(CartesianPoint(3, 4))
    ppp = pp * 50
    print(ppp)
    print(p - pp)
    print(p)
    print(p.polar)
    print(p.add_cartesian(CartesianPoint(4, 5)))
    # print(p.add_polar(Point(1, 2)))
    p.set(p.add(Point(CartesianPoint(4.3, 5.5))))
    print(p)
    # print(p.add_polar(Point(1, 2)))
    # print(p.set(p.add_polar(1)))
