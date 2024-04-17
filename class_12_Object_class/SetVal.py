class MyTest:
    name=""
    def showName(self):
         print(f"Name is:{self.name}");
    def setVal(self,name):
        self.name=name

newObject=MyTest()
newOb=MyTest()
newOb.setVal("Islam")
newObject.name="Nazir"
newObject.showName()
newOb.showName()