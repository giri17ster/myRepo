class Car:

    #static/class variable
    wheels = 4

    def __init__(self):
        #instance variables
        self.mileage = 15
        self.color = "Grey"

    @classmethod
    def getWheels(cls):
        print(cls.wheels)

    @staticmethod
    def staticMethodExample():
        print("inside static example method")

c1 = Car()
c2 = Car()

print(c1.color,c1.mileage,Car.wheels)
print(c2.color,c2.mileage,Car.wheels)

print(Car.getWheels())
print(c2.getWheels())