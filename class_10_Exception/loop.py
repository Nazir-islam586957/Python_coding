a=int(input("Enter 1st Value="))
b=int(input("Enter 2nd Value="))
try:
    a=a/b
    m=[11,22,'apple','Orange']
    print("result is=",a)
    print("Value of 5th index=",m[5])

except IndexError:
    print("Error is IndexError")
except ZeroDivisionError:
    print("Erroris ZeroDivistionError")

except ValueError:
    print("Error is ValueError")

except Exception:
    print("Error is Exception")
finally:
    print("Hello World")