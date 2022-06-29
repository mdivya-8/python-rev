
print('hello')
hello
10+20
30
_
30
_*3
90
_+2
92
_
92
1**2
1
2**2
4
2**3
8
for i in range(1,11):
    print("7","*",i,"=",7*i)

    
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
7 * 10 = 70
s="hello"
s*3
'hellohellohello'
s.upper()
'HELLO'
x='APPLE'
x.lower()
'apple'
x=apple
#multiple assignment
      
a=b=c=5
      
print(a,b,c)
      
5 5 5
print(a,b)
      
5 5
a,b,c,d=10,'apple',12.4,'s'
      
print(a,b,c,d)
      
10 apple 12.4 s
type(a)  # type()function
      
<class 'int'>
type(b)
      
<class 'str'>
type(c)
      
<class 'float'>
type(d)
      
<class 'str'>
print(d,c,b,a)
      
s 12.4 apple 10
#format()function
txt="my name is {fname},I'm {age}years old.".format(fname="dolly",age=3)
      
txt
      
"my name is dolly,I'm 3years old."
txt="my name is {},I'm {}years old.".format("dolly",3)
      
txt
      
"my name is dolly,I'm 3years old."
txt="my name is {0},I'm {1}years old.".format("dolly",3)
      
txt
      
"my name is dolly,I'm 3years old."
#id()function
id(1)
      
2354217550064
x=1
      
id(x)
      
2354217550064
y='s'
      
id(y)
      
2354218372272
id(1)
      
2354217550064
id(2)
      
2354217550096
id(1)-id(2)
      
-32
x=1
      
y=2
      
print(x is y)
      
False
y=1
      
print(x is y)
True
x='python'
'p' in x
True
's' in x
False
's' not in x
True
x=["apple","banana"]
y=["cat","dog"]
z=x
print(z)
['apple', 'banana']
print("memory location of x=",id(x))
memory location of x= 2831653763200
print("memory location of x=",id(x))
memory location of x= 2831653763200
print("memory location of x=",id(z))
memory location of x= 2831653763200
print(x is z)
True
print(x is y)
False
print(x is not y)
True
for a in [1,2]:
    for b in [1,2]:
        print(a,b)

        
1 1
1 2
2 1
2 2

'''def m1():
    a=10   #local variable
    print(a)  
    return
def m2():
    print(a) #name error
    return
m1()
m2()
def m1():
    a=10  #local to m1
    print(a)
    return
def m2():
    a=90
    print(a)  #local to m2
    return
m1()
m2()
a=10   #global variable
def m1():
   
    print(a)
    return
def m2():
    
    print(a)
    return
m1()
m2()
a=10
def m1():
   
    print(a)
    return
def m2():
    a=65
    print(a)
    return
m1()
m2()
  
def m1():
    a=65
    a=a+10
    print(a)
    return
m1()
a=65
def m1():
    global a
    a=a+10
    print(a)
    return
m1()
def func():
    print("case")
    return
func()
def func():
    print("case")
    return 200
x=func()
print(x)
def func(a,b):
    print("a:",a)
    print("b:",b)
    return
   
func(10,20)

def func(a,b):
    print("a:",a)
    print("b:",b)
    return a*b
   
print(func(10,20))'''



