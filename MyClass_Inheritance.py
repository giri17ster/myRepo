class Animal:
    def printColor(self):
        print("Animal printColor")
    def printWeight(self):
        print("Animal printWeight")
class Cat(Animal):
    def printColor(self):
        print("Cat printColor")

c1 = Cat()
c1.printColor()
c1.printWeight()