class OuterClass:
    def __init__(self, outer_val):
        self.outer_val = outer_val
        self.inner_class_instance = self.InnerClass()

    def outer_method(self):
        print("This is outer method")
        self.inner_class_instance.inner_method()

    class InnerClass:
        def __init__(self):
            pass

        def inner_method(self):
            print("This is inner method")


# Creating an instance of the outer class
outer_instance = OuterClass("Outer")

# Calling the outer method which in turn calls the inner method
outer_instance.outer_method()
