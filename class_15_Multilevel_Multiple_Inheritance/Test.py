class My:
    x=300
    def add(self,y):
        self.x=self.x+y
        return self.x
    def show(self):
        print("This is my show")

class Hello(My):
    def show(self):
        print("Hello Show")
    def dis(self):
        print("This is Hello Display")

class Test(Hello,My):
    def wel(self):
        print("Welcome to Utc")

hello=Test()

# hello=Hello()
hello.show()
hello.dis()
print("Add is =",hello.add(12))
