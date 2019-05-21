
class Computer:
    def __init__(self,ram,make):
        self.ram=ram
        self.make=make

    def compare(self,instance2):
        if self.make==instance2.make:
            return True
        else:
            return False
c1=Computer(6,"Dell")
c2=Computer(6,"Dell")

print(c1.compare(c2))
