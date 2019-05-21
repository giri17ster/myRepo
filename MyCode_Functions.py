#normal function, not accepting or returning anything
def greetMe():
    print("Hello!")
    print("How are you?")

greetMe()

#accepting parameters return nothing
def addNumbers(a,b):
    print(a+b)

addNumbers(2,3)

#return from function
def addNumbers1(a,b):
    return a+b

print(addNumbers1(4,5))

#return multiple values
def add_sub(a,b):
    return a+b,a-b

return1,return2 = add_sub(5,2)
print(return1,return2)
