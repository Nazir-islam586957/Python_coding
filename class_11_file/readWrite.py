
try:
    myFile=open("test.txt",'r')
    myFile2=open("test3.txt",'w')
    a=myFile.read();
    myFile2.write(a);
    print(a)
    myFile.close()
    myFile2.close()
except FileExistsError:print("No File Exist")
except FileNotFoundError:print("No File Found")
finally:print("Hello")
print("Bangladesh")