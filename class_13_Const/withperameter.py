class Hello:
    x = 0
    def __init__(self,x):
        self.x=x
        print("Hello")
    def showNum(self, n):
        while self.x<n:
            self.x = self.x+1;
            print("Number is=", self.x)


obj = Hello(2)
print("Value of x=")
obj.showNum(10)
