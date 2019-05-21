def modifyValues(a):
    print("before changing value -",id(a))
    a = 8
    print("after changing value - ", id(a))
    print("a-",a)

input = 10
#pass by value
print("original id -", id(input))
modifyValues(input)
print("input-",input)

print("*****************************")

def modifyList(lst):
    print("before changing value -", id(lst))
    lst[1] = 15
    print("after changing value - ", id(lst))
    print("lst-", lst)


lst = [10,12,14]
# pass by value
print("original id -", id(lst))
modifyList(lst)
print("lst-", lst)