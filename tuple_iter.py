# An iterator is an object that contains a countable number of values
#lists,tupels,dictionaries,and sets are all iterable object.
#An iterator from a tuple
mytuple=("cherry","banana","apple")
myit=iter(mytuple)
'''print(next(myit))
print(next(myit))
print(next(myit))'''
for i in mytuple:
    print(i)
