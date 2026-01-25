from abc import ABC, abstractmethod
class ABCclass(ABC):
    def print(self, x):
        print("The value passed is:",x)
    @abstractmethod
    def task(self):
        print("We are inside an ABCclass task")
class test_class(ABCclass):
    def task(self):
        print("We are inside the test_class task")
test_obj= test_class()
test_obj.task()
test_obj.print(100)