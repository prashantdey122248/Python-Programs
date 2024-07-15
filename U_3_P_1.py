class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

    def add_numbers(self, a, b):
        result = a + b
        print(f"The sum of {a} and {b} is {result}")

# Create an instance of the class
obj = MyClass("Alice")

# Call the methods
obj.greet()
obj.add_numbers(3, 5)
