from math import sqrt
from math import abs
class Point:

    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def dist_to(self, p):
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)


    def abs(self):
        return sqrt(self.x**2 + self.y**2)
class Rectangle:

    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2


    def area(self):
        return (abs(self.corner1.x - self.corner2.x)*abs(self.corner1.y - self.corner2.y))
    def perimeter(self):
        return (abs(self.corner1.x - self.corner2.x)*2 + abs(self.corner1.y - self.corner2.y)*2)

class Circle:

    def __init__(self,center,radius):
        self.center = center
        self.radius = radius

    def inside(self, circpoint):
        if circpoint.dist_to(center) > self.radius:
            print("It is not within the circle.")
        else:
            print("It is within the circle.")
    def area(self):
        return(self.radius*self.radius*3.14)
    def perimeter(self):
        return(self.radius*2*3.14)
def main():
    p1 = Point(3.0, 4.0)
    print("The point ({}, {}) is at a distance of {} from the origin.".format(p1.x, p1.y, p1.abs()))

    p2 = Point(-1.0, 6.5)
    print("It is a distance {:.5} away from the point ({}, {}).".format(p1.dist_to(p2), p2.x, p2.y))

    r= Rectangle(Point(1,1),Point(4,5))
    print("The area of the rectangle is " + str(r.area))
    print("The perimeter of the rectangle is " + str(r.perimeter))
    c= Circle(Point(-2,3),2)
    print("The area of the circle is " + str(c.area))
    print("The perimeter of the circle is " + str(c.perimeter))
    c.inside(Point(0,1))


if __name__ == "__main__":
    main()
