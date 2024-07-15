#WAP to create abstract class with one method.
from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass

# Example subclass implementing the abstract method
class MySubclass(MyAbstractClass):
    def my_abstract_method(self):
        print("Implemented abstract method")

# Instantiating the subclass
obj = MySubclass()
obj.my_abstract_method()
