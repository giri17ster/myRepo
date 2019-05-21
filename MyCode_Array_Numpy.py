from numpy import *

vals = array([1,2,3,4,5])

print(vals)
print(type(vals))
print(vals.dtype)

vals = array([1,2.0,3,4,5])
print(vals)
print(type(vals))
print(vals.dtype)

#linspace
vals = linspace(0,10,4)
print(vals)

#linspace - by default 50 parts
vals = linspace(0,8)
print(vals)

# arange - mention difference as last param
vals = arange(1,10,2)
print(vals)

#logspace
vals = logspace(1,20,2)
print(vals)

#zeros
vals = zeros(10)
print(vals)

#ones
vals = ones(5)
print(vals)