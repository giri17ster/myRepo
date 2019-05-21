from numpy import *

vals = array([
                [1,2,3,11,12,13],
                [4,5,6,14,15,16]
            ])
#array dimentions
print(vals.ndim)

#number of rows and columns
print(vals.shape)

#total number of elements
print(vals.size)

#convert two dimentional to one dimention
vals1=vals.flatten()

print(vals1)

#convert from single to multidimention array
vals2 = vals1.reshape(3,4)
print(vals2)

print("**********************************")

vals3 = vals1.reshape(2,2,3)
print(vals3)

print("**********************************")

m = asmatrix(vals)
print(m)

print("**********************************")

m1 = asmatrix('1,2,3 ; 4,5,6; 7,8,9')
m2 = asmatrix('1,2,3 ; 4,5,6; 7,8,9')

print(m1+m2)

print("**********************************")

print(m1*m2)