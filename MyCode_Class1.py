
class MyClass:

    def __init__(self,m,n):
        print("in init")
        self.m=m
        self.n=n

    def printDetails(self):
        print("Inside printDetails")
        print("First param - ",self.m)
        print("Second param - ", self.n)

a = 10
myclass = MyClass(115,120)
print(type(myclass))
print(myclass.printDetails())
print(MyClass.printDetails(myclass))
print(myclass.m, myclass.n)