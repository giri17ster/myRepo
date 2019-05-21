from numpy import *
vals = array([1,2,3,4,5])

#create new array with element = elements of above array *5
vals = vals*5

print(vals)

vals1 = array([5,4,3,2,1])

#create array with addition of above arrays
vals3 = vals+vals1
print(vals3)

#sum of all elements of array
print(sum(vals))

#concatinate two arrays
print(concatenate([vals1,vals3]))

#copying the array
vals4 = vals

print(vals4)
print(id(vals))
print(id(vals4))

#shallow copy
vals4 = vals.view()
vals[0]=7
print(vals4)
print(id(vals))
print(id(vals4))

#deep copy
vals4 = vals.copy()
vals[0]=8
print(vals4)
print(id(vals))
print(id(vals4))

