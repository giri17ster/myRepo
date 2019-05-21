#normal declaration
def employee(name,age):
    print(name,age)

employee("Girish",31)

#keywords
def employee1(name,age):
    print(name,age)
employee1(age=31,name="Girish")

#default
def employee2(age,name="Girish"):
    print(name,age)
employee2(age=31)

#variable length
def sum(a,*b):
    c = a
    for i in b:
        c += i
    print(c)

sum(1,2,3,4)
