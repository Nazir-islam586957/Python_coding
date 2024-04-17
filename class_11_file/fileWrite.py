
try:
    a=input("Enter Data=")
    myFile=open("test2.txt",'w')
    data=myFile.write(a);
    myFile.close()
except FileExistsError:print("No File Exist")
except FileNotFoundError:print("No File Found")
finally:print("Hello")
print("Bangladesh")