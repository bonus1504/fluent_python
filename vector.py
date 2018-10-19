from math import hypot


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return 'Vector({!r}, {!r})'.format(self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __bool__(self):
        return bool(self.x or self.y)
