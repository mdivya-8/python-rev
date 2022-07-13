#user-defined functions
'''x=5;
y=3;
def add(x,y):
    add=x+y
    print("sum:",add)
    return add
add(x,y)
def average(x,y):
    average=(x+y)/2
    print("average:",average)
    return
average(x,y)
def power(x,y):
    power=(x**y)
    print("power:",power)
    return
power(x,y)

name="thundersoft"; #globally create one string 
def string_name():  #fun defination 
    n=len(name); # to find length of the str
    return
print(name+ " is a company")
print(len(name))   #print str length
print(name[2:])    # print from second index
print(name[:2])     #print the str upto second index
string_name()   '''  #fun call

#default arguments function
def defaultArgs(a,b,c,d=40):
    print("a=",a,"b=",b,"c=",c)
    return
defaultArgs(11,22,33)
defaultArgs("java","python","c+")
defaultArgs(11,22,33,44)
defaultArgs(11,22,"os","git")
 #required argument function
def requiredArgs(l,m,n):
    print("l=",l,"m=",m,"n=",n)
    return
requiredArgs(10,20,30)
requiredArgs("string","tuple","list")
requiredArgs(10,20,"juice")
#keyword arguments
def keywordArgs(emp,exp):
    print(emp,"exp= ",exp)
    return
keywordArgs(emp="abc",exp=10)#keys must and should to accept it values
keywordArgs(emp="def",exp=32)
keywordArgs(emp="ghi",exp=12)
#variable argument function
def variableArgs(*a):
    print("list:",a)
    return
variableArgs(10)#it accepts no of arguments
variableArgs(10,20,30,40)
variableArgs(10,300,"python")
variableArgs(100,"list","python","june","july")
#lambda function  lambda function can take any number of arguements,but can only have one expression
x = lambda a : a + 10
print(x(5))
a = 40
b = 40
x = lambda a,b: a+b
print("sum = ", x(a,b))
aa=20
bb=30
xy=lambda aa,bb: aa*bb
print("multiplication:",xy(aa,bb))

#filter
thunder=[1,5,4,6,8,11,3,12]
even=filter(lambda x:x%2==0,thunder)
print(list(even))

odd=filter(lambda x:x%2!=0,thunder)
print(list(odd))

thundersoft=[10,13,21,40,15,3,224,560,34]
even1=filter(lambda xx:xx%2==0,thundersoft)
print("even numbers:",list(even1))
odd1=filter(lambda xx:xx%2!=0,thundersoft)
print("odd numbers:",list(odd1))
#map
jonh=[1,3,2,4,5,6,7,8,9]
var=map(lambda x:x*2,jonh)
print(list(var))
var1=map(lambda y:y%2==0,jonh)
print(tuple(var1))
