Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.



from math import pi

class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def area_of_circle(self):
        area = pi * self.radius**2
        return area
    
    def perimeter_of_the_circle(self):
        perimeter = 2 * pi * self.radius
        return perimeter


radius = float(input("Enter the radius of the circle: "))
c = Circle(radius)
print(c.area_of_circle())
print(c.perimeter_of_the_circle())
