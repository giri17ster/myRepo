from array import *

vals = array('i',[1,2,3,4,5])

print (vals.buffer_info())
print(vals.typecode)
vals.reverse()
print(vals)
print(vals[0])

#iterate array using for loop
for i in vals:
    print(i,end="")

#iterate array using while loop
i = 0
while i<len(vals):
    print(vals[i])
    i+=1

#clone array
vals1=array(vals.typecode,(a for a in vals))
print(vals1)

#create new array whos elements are in a pattern a**a from first array elements
vals2=array(vals.typecode,(a**a for a in vals))
print(vals2)