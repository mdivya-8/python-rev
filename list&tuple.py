
# Different types of tuples

# Empty tuple
'''my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)
#indexing
# Accessing tuple elements using indexing
my_tuple = ('p','e','r','m','i','t')

print(my_tuple[0])   # 'p' 
print(my_tuple[5])   # 't'
# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])       # 's'
print(n_tuple[1][1])       # 4
#negative indexing
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')

# Output: 't'
print(my_tuple[-1])

# Output: 'p'
print(my_tuple[-6])
#slicing
my_tuple = ('p','r','o','g','r','a','m','i','z')

# elements 2nd to 4th
# Output: ('r', 'o', 'g')
print(my_tuple[1:4])

# elements beginning to 2nd
# Output: ('p', 'r')
print(my_tuple[:-7])

# elements 8th to end
# Output: ('i', 'z')
print(my_tuple[7:])

# elements beginning to end
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple[:]) '''
#methods
#index method
'''val = ('a','b','r','a','k','a','d','h','a')  
print(val)  
index = val.index('k')   
print("Index of k is: ",index)'''
#count method
'''a = (2,4,6,8,10)  
print(a)    
count = a.count(10)  
print("Occurences:",count) '''
#built in functions
#len
tuple = ("apple", "banana", "cherry")
print(len(tuple))
#all()
a=(1,0,1)
print(all(a))
#any()
a=(3,6,0)
print(any(a))
#enumarate()
a=(11,22,33)
print(list(enumerate(a)))
#sum()
a=(4,6,7,8)
print(sum(a))
#max()
a=(6,7,8,9)
print(max(a))
#min()
a=(6,7,8,9)
print(min(a))

# list by iterator
'''mytuple=("cherry","banana","apple")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
for i in mytuple:
    print(i)'''

#finding len of list
'''l=[20,50,60,40]
n=len(l)
print("lenght:",n)
for i in range(0,n):
    print(i,l[i])'''
#copy,append
'''a=[10,30,40,50,70,80]
print("a is :",a)
b=a.copy()
print("b is :",b)
b.append(488)
print(b)'''
#extend
'''list=[20,400,500,600,7]
list.extend([10,20,[50,66],44])
print(list)'''
#remove

'''list=[20,30,40,50]
list.remove(30)
print(list)'''
#count
'''list=[33,55,6,6,88]
c=list.count(6)
print(c)'''
#sort
'''list=[11,3,45,6,77,88,9,20]
list.sort()
print("sorted:",list)
list.sort(reverse=True)
print("descending order:",list)
list.sort(reverse=False)
print("asecnding order:",list)'''
#clear
'''list=['apple','ball','cat']
list.clear()
print(list)'''
#insert
'''list=[2,'abc',4]
list.insert(1,'apple')
print(list)'''
#pop
'''list=[2,'apple','abc',4]
list.pop(1)
print(list)'''
#index
'''list=[44,66,77,8]
x=list.index(66)
print(x)'''
#reverse
'''list=[1,2,3,4]
list.reverse()
print(list)'''
#built in functions in list
#all(),any(),enumarate(),len() ,list(),max(),min()                   
a=['True',1,4,6,7]
b=[1,0,50,77]
print(all(a))
print(any(a))
print(all(b))
print(any(b))
print("length of a:",len(a))
print("max element is:",max(b))
print("min element is:",min(b))
print("list of the elementas is:",list(a+b))
for i in enumerate([1,2,3,4,'mango',6,50]):
    print(i)

