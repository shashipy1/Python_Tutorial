# from abc import ABCMeta, abstractmethod
# class Shape(metaclass=ABCMeta):

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 5
        self.breath =4

    def printarea(self):
        return self.length * self.breath

rect1 = Rectangle()
print(rect1.printarea())
# tryobj = share() IT IS NOT POSSIBLE B/C IT DON'T SPORTED