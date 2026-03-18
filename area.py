class Area:

    def __init__(self):
        self.r = int(input("Enter radius: "))
        self.h = int(input("Enter height: "))

    def circle_area(self):
        return 3.14 * self.r * self.r

    def cylinder_area(self):
        return 2 * 3.14 * self.r * (self.r + self.h)

    def cone_area(self):
        return 3.14 * self.r * (self.r + self.h)

    def cylinder_volume(self):
        return 3.14 * self.r * self.r * self.h

    def cone_volume(self):
        return (1 / 3) * 3.14 * self.r * self.r * self.h


obj = Area()

print("Area of Circle:", obj.circle_area())
print("Area of Cylinder:", obj.cylinder_area())
print("Area of Cone:", obj.cone_area())
print("Volume of Cylinder:", obj.cylinder_volume())
print("Volume of Cone:", obj.cone_volume())
