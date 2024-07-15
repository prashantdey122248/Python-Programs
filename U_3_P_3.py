class Circle:
    # Class variable
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    # Instance method
    def area(self):
        return self.pi * self.radius ** 2

    # Instance method
    def circumference(self):
        return 2 * self.pi * self.radius

    # Class method
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

# Creating an instance of Circle
circle1 = Circle(5)
print("Radius:", circle1.radius)
print("Area:", circle1.area())
print("Circumference:", circle1.circumference())

# Creating another instance using the class method
circle2 = Circle.from_diameter(10)
print("\nRadius:", circle2.radius)
print("Area:", circle2.area())
print("Circumference:", circle2.circumference())
