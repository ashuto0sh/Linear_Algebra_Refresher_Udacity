from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec=30

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
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
        return Decimal(sqrt(l_2))

    def Norm(self):
        try:
            l=self.Length()
            r=[x*Decimal('1.0')/l for x in self.coordinates]
        except ZeroDivisionError:
            raise Exception('Zero vector can not be normalized')

        return Vector(r)

    def Dot(self, other):
        r=sum([x*y for x, y in zip(self.coordinates, other.coordinates)])
        return Decimal(r)

    def AngleWith(self, other, in_degrees=False, epsilon=1e-10):
        d=self.Dot(other)
        sl, ol=self.Length(), other.Length()

        try:
            k=d/(sl*ol)
            if k-1>epsilon:
                k=1
            elif k+1<epsilon:
                k=-1
            angle=acos(k)
            if in_degrees==True:
                angle=angle*180.0/pi
        except ZeroDivisionError:
            raise ZeroDivisionError('Unable to find angle with zero vector(s)')

        return angle

    def IsZero(self, epsilon=1e-10):
        return self.Length() < epsilon

    def IsParallel(self, other, epsilon=1e-10):
        if self.IsZero() or other.IsZero() or abs(self.AngleWith(other))<epsilon or abs(self.AngleWith(other)-pi)<epsilon:
            return True
        return False

    def IsOrtho(self, other, epsilon=1e-10):
        if self.IsZero() or other.IsZero() or abs(self.Dot(other))<epsilon:
            return True
        return False

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates
