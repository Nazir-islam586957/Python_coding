
class Hello:
     x=0
     def showNum(self,n):
         while self.x<n:
             self.x=self.x+1;
             print("Number is=",self.x)
obj=Hello()
obj.showNum(10)
 