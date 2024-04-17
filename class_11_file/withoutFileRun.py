
try:
    myFile=open("test2.txt",'r')
    data=myFile.read();
    print(data)
    myFile.close()
except FileExistsError:print("No File Exist")
except FileNotFoundError:print("No File Found")
finally:print("Hello")
print("Bangladesh")