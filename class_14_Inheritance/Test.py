class Hello:
    x=0
    def showNum(self,n):
        while self.x<n:
            self.x=self.x+1;
            print("Number is=",self.x)

class hi(Hello):
    def add(self,a,b):
        a=a+b
        print("Add is=",a)
    def showNum(self,n):
        n=n*10
        print("Multi is=",n)
obj = hi()
print("Value of x=",obj.x)
obj.showNum(10)
