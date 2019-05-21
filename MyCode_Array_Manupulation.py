from array import *
#create array with dynamic length
vals = array('i',[])

arrayLength = int(input("Enter the array size - "))
for i in range(arrayLength):
    vals.append(int(input("Enter value - ")))

print(vals)

#index of required element
searchElement = int(input("Enter the element - "))
k = 0
for e in vals:
    if e==searchElement:
        print(k)
        break;
    k+=1

#index of required element with function
print(vals.index(searchElement))