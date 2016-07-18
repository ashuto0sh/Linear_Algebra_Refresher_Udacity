from math import sqrt

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __isSameLen(self, v):
        return self.dimension==v.dimension

    def __add__(self, other):
        try:
            if not self.__isSameLen(other):
                raise ValueError
        except ValueError:
            raise ValueError('Addition requires vectors of same length')

        r=[x+y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(r)

    def __sub__(self, other):
        try:
            if not self.__isSameLen(other):
                raise ValueError
        except ValueError:
            raise ValueError('Subtraction requires vectors of same length')

        r=[x-y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(r)

    def __mul__(self, scalar):
        r=[scalar*x for x in self.coordinates]
        return Vector(r)

    def __rmul__(self, scalar):
        r=[scalar*x for x in self.coordinates]
        return Vector(r)

    def Length(self):
        l_2=sum([x**2 for x in self.coordinates])
        return sqrt(l_2)

    def Norm(self):
        try:
            l=self.Length()*1.0
            r=[x/l for x in self.coordinates]
        except ZeroDivisionError:
            raise Exception('Zero vector can not be normalized')

        return Vector(r)

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates
