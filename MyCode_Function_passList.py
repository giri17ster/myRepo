
def returnEven(lst):
    count=0
    lst1=[]
    for i in lst:
        if i%2==0:
            lst1[count]=i
    return lst1

print(returnEven([1,2,3,4,5]))