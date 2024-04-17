from abc import ABC,abstractmethod

class Test(ABC):
    # @abstractmethod
    def add(self,a,b):
        pass

    def show(self):
        print("This is Show")

class My(Test):
    def hello(self):
        print("Hello My Test Class")

ob=My()
ob.show()
ob.hello()