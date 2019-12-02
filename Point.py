import math
from collections import namedtuple


class Point:
    _x = 0.0
    _y = 0.0
    _r = 0.0
    _theta = 0.0
    p = namedtuple('pp', ('x', 'y'))

    def __init__(self, x=0, y=0):
        self._x = round(x, 2)
        self._y = round(y,2)
        self._polar(x, y)
        self.get_cartesian = self.get_cartesian()


    def _polar(self, x, y):
        self._r = math.sqrt(x**2 + y**2)
        if y == 0:
            self._theta = 0
            return
        if x == 0:
            self._theta = math.atan(float('inf'))
            return
        self._theta = math.atan(y/x)

    def _cartesian(self, r, theta):
        self._x = r * math.sin(theta)
        self._y = r * math.cos(theta)

    def set_polar(self, r, theta):
        self._r = r
        self._theta = theta
        self._cartesian(r, theta)

    def set_cartesian(self, x, y):
        self._x = x
        self._y = y
        self._polar(x, y)

    def get_cartesian(self):
        # self.pp(self._y, self._y)
        return self._x, self._y

    def get_polar(self):
        return self._r, self._theta

    def distance(self, point):
        return math.sqrt(pow(self._x - point._x,2) + pow(self._y - point._y, 2))

    def add(self, point):
        return Point(self._x + point._x, self._y + point._y)

    def add_polar(self, r, theta):
        return Point(self._x + r * math.cos(theta), self._y + r * math.sin(theta))

    def to_string(self):
        return "(" + str(self._x) + ", " + str(self._y) + ")"
