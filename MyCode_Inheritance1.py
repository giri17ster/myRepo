class A:
    def __init__(self):
        print("Inside A init")
    def feature1(self):
        print("Inside feature1")

class B:
    def __init__(self):
        print("Inside B init")
    def feature2(self):
        print("Inside feature2")

class C(B,A):
    def __init__(self):
        print("Inside C init")
        super().__init__()
    def feature3(self):
        print("Inside feature3")
        super().feature2()

c1=C()
c1.feature3()
