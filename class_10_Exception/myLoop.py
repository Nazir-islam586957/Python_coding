a=int(input("Enter 1st Value="))
b=int(input("Enter 2nd Value="))
try:
    a=a/b
except ZeroDivisionError:
    print("Result is=",a)
print("Hello World")