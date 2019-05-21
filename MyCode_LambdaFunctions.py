from functools import reduce

f = lambda a: a+a

print(f(15))

lst = [1,2,3,4,5,6,7,8,9,10]

#create a list of even numbers from above list
print(list(filter(lambda a : a % 2 == 0,lst)))

#create a list where each element from above list is doubled
print(list(map(lambda a:a*2,lst)))

#print the list of sum of all elements from list
print(reduce(lambda a,b:a+b,lst))

#print the list of odd numbers
print(list(filter(lambda a:a%2!=0,lst)))
