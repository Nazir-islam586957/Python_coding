class Hello:
    x=0
    def __init__(self,m):
        print("Hello",m)
    def showNum(self,n):
        while self.x<n:
            self.x=self.x+1
            print("Number is=",self.x)
class hi(Hello):
    def add(self,a,b):
        a=a+b
        print("Add is=",a)

    def __init__(self):
        print("Welcome to utc")

    def showNum(self,n):
        n=n*10
        print("Multi is=",n)
class my(hi):
    def test(self):print("Test")
obj = my()
print("Value of x=",obj.x)
obj.showNum(10)
obj.add(15,3)
