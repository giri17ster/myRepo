
a = 10
b = 20

def printNumber():
    global a
    a = 15
    print(a)

    b=25
    globals()['b']=30
    print("local b - ",b,", Global b - ",globals()['b'])

printNumber()

print(a)