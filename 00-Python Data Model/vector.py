from math import  hypot

"""
Vector.py a simplistic Class demostrating some special methods

it is a simplistic for didactic reasons. it lacks proper error handling, 

special methods ``__add__`` ,  ``__mull__``


add:
>>> v1 = Vector(2, 4)
>>> v2 = Vector(2, 1)
>>>> v1 + v2
Vector(4, 5)

Absolute Value:

>>>> v = Vector(3, 4)
>>>> abs(v)
5.0


scalar Multiplication:

>>>> v * 3
vector(9, 12)

>>>> abs(v * 3)
15.0

"""

class Vector:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector({self.x!r} , {self.y!r})'

    """def __str__(self) -> str:
        return f'Vector({self.x!r}, {self.y!r})' """
    
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __bool__(self):
        return bool(self.x or self.y)


def main():

    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print(v1 + v2)


    v = Vector(3, 4)
    print(abs(v))

    print(v * 3)

    print(bool(v1))



if __name__ =='__main__':
    main()