
impor csv
cs=et=hw=nw=ma=pr=0
# cs=pr=nw=et=ma=hw=0

# opening the CSV file
with open('student_data.csv',mode='r')as file:

# reading the CSV file
csvFile=csv.reader(file)  

# displaying the contents of the CSV file  
for liens in csvFile:
    if("Computer science core sub"==liens[0]):
        cs=cs+1
    elif("Programming"==liens[0]):
        pr=pr+1
    elif("Networking"==liens[0]):
        nw=nw+1
    elif("Electrical & Electronics"==liens[0]):
        et=et+1
    elif("Mathematics"==liens[0]):
        ma=ma+1
    elif("Hardware"==liens[0]):
        hw=hw+1

print("CS",cs,"\nprogramming=",pr,"\nNetworking=",nw,
    "\nElectric",et,"\nMathmatics",ma,"\nHardware",)