from threading import *
class A(Thread):
    def run(self):
        print(Thread.getName(self))

class B(Thread):
    def run(self):
        print(Thread.getName(self))

t1 = A()
t2 = B()

t1.start();
t2.start();