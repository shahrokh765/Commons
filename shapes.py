import abc
from Commons.Point import Point
from typing import List
from random import randint
import warnings


class Shape(abc.ABC):

    @abc.abstractmethod
    def points(self, n: int) -> List[Point]:
        """:param n: number of random points to be returned
        :return: return a List of Point objects"""
        pass

    @abc.abstractmethod
    def all_points(self) -> List[Point]:
        """:return: return all the points in the shape"""
        pass

    @abc.abstractmethod
    def __str__(self):
        pass


class Rectangle(Shape):
    """Create Rectangle object given length and width originated in Point(0, 0)"""
    def __init__(self, width: int, length: int):
        self.__width = width
        self.__length = length

    def points(self, n: int) -> List[Point]:
        if n > self.length * self.width:
            warnings.warn("Number of Points requested is more than all the points. Duplicates exist.")
        return [Point((randint(0, self.width - 1), randint(0, self.length - 1))) for _ in range(n)]

    def all_points(self):
        return [Point((x, y)) for x in range(self.width) for y in range(self.length)]

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    def __str__(self):
        return "{tp}: width= {wd}, length= {len}".format(tp=type(self).__name__, wd=self.width, len=self.length)


class Square(Rectangle):

    def __init__(self, side):
        Rectangle.__init__(self, side, side)


if __name__ == "__main__":
    rect1 = Rectangle(10, 20)
    print(rect1)
    for point in rect1.points(10):
        print(point)
    print('All points')
    for point in rect1.all_points():
        print(point)

    sq1 = Square(4)
    print(sq1)
    for point in sq1.points(20):
        print(point)
    print('All points')
    for point in sq1.all_points():
        print(point)
