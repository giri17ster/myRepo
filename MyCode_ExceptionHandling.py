a = 9
b = 0

try:
    print(a/b)
except Exception as e:
    print("Error - ",e)
except ZeroDivisionError as z:
    print("Error - ",z)
finally:
    print("Inside finally")