from math import pi


class Shape:
    def __init__(self, r=0, l=0, w=0):
        self.radius = r
        self.length = l
        self.width = w

    def area1(self):
        return r * r * pi

    def per1(self):
        return r * 2 * pi

    def area2(self):
        return l * w

    def per2(self):
        return (l + w) * 2


shape = input("Shape name (1:Circle | 2:Rectangle) : ")

if shape == "1":
    r = int(input("Radius : "))
    circle = Shape(r=r)
    print("Area :", circle.area1())
    print("Perimeter :", circle.per1())

elif shape == "2":
    l = int(input("Length : "))
    w = int(input("Width : "))
    rectangle = Shape(l=l, w=w)
    print("Area :", rectangle.area2())
    print("Perimeter :", rectangle.per2())
