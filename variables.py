print("Hello python")
print("hello thundersoft")
var="mango"
print(var)
var1=100,1000   #assigning
print(var1)
var11,var2=200,300  #assigning
print(var11,var2)
language="python"   #format
print("welcome to {0}".format(language))

a=50    
b="mango_appple"
c=a+8j
print(type(a))  #int
print(type(b))  #string
print(type(c))   #complex
var11=str(40)
var12=int(40)
var13=float(40)
print(var11)   #string --->40
print(var12)   #int--->40
print(var13)    #float--->40.0

a=30
A=40
A=50  
print(a)
print(A)       #print updated one


myvar="john"
my_var="john"
_my_var="tom"
myVar="tomson"
MYVAR="tommy"
myvar2="jonny"
#camel case
myVarName="python"
print("camel case:",myVarName)
#pascal case
MyVarName="data structure"
print("pascal case:",MyVarName)

#many values to multiple variables
x,y,z="orrange","apple","grapes"
print(x)
print(y)
print(z)
print(x,y,z)
#single value to a multiple variables
x=y=z="hyderabad"
print(x)
print(y)
print(z)
print(x,y,z)

#unpack a collection
fruits=["banana","mango","custerd apple"]
x,y,z=fruits
print(x)
print(y)
print(z)
print(x,y,z)
x=y=z=fruits
print(x)
print(y)
print(z)

#print function
a="python is awsome"
print(a)
m="python"
n="is a"
o="wonderful"
print("m,n,o",m,n,o)
print("m+n+o:",m+n+o)
print(m+n)
print(o,m)

xx=10
yy=20
zz="johny"
print(xx+yy)
print(xx*yy)
print(xx,yy,zz)
#print(xx+yy+zz) not supportted 'str' & 'int'

#global variables
xl="awesome"
def myfun():
    print("python is ",xl)
    print("python is " +xl)
    #print("python is",myfun(xl))
myfun()
#global & local variables
alex="extraordinary"
def myfun():
    alex="fantastic"
    print("my dad thoughts are ",alex)
myfun()
print("my mom cooking was ",alex)

#global keyword

def myfun():
    global xs
    xs="wonderful"
    print("island is a ",xs)
myfun()
print('germany is a ',xs)

      #global keyword
ml="wonderla"
def myfun():
    global ml
    ml="mini_wonderla"
    print("i am going ",ml)
myfun()
print(" we're going ",ml)

#re_declaration
age=50
print("my age is:",age)
age=55
print("her age us :",age)

a=b=c="shift"
print(a)
print(b)
print(c)
a,b,c=40,50,'amer'
print(a)
print(b)
print(c)

#constants
maxi=30
maxi1='g'
maxi2="strings are available"
print(maxi)
print(maxi1)
print(maxi2)

#literals
    #1.numeric literals
intVar=100
floatVar=20.5
complexVar=complex(1,3)
print(intVar)
print(floatVar)
print(complexVar)
     #string literals
strVar="python"
print(strVar)
     #BooleanVar
boolVar=True
print(boolVar)
      #abscence literals
noneVar=None
print(noneVar)
     #list literals
listVar=[10,20,38,59670]
print(listVar)
   #tupleVar
tupleVar=(1,2,34,4,5)
print(tupleVar)
    #setVar
setVar={1,2,2,4,5,5}
print(setVar)
     #dictVar
dictVar={1:"apple",2:"banana",3:"carrot"}
print(dictVar)
#format function
txt="my name {fname}.My age is {fage},i am from {fplace}".format(fname="divya",fage=23,fplace="chittoor")
print(txt)
txt1="i am {} girl, i am {}."
print(txt1.format("strenght","supporter"))
txt2=" my father is my {0},he is my {1}."
print(txt2.format("hero","world"))

#data conversions
int1=200
ffloat=40.0
b=True
c=143
  #converting to int
print(int(int1))
print(int(ffloat))
print(int(b))
print(int(c))
    #converting to float
print(float(int1))
print(float(ffloat))
print(float(b))
print(float(c))
     #converting to complex
print(complex(int1))
print(complex(ffloat))
print(complex(b))
print(complex(c))
     #converting to char
print(chr(int1))
#print(chr(ffloat))     #float cannot converted into int
print(chr(b))
print(chr(c))


#math operations
import math
b=math.ceil(10.6)
print("ceil value  of 10.6 is:",b)
'''a=10
b=30
math.cmp(a,b)
print(math)'''
z=math.floor(10.4)
print("flor value of 10 is:",z)
#math.abs(-10)
#print("absolute value of 10 is:",math.abs(-40))

#id () functions
string1="hello world"
str2=set(string1)
print(str2)
print(id(str2))
str3=list(string1)
print(str3)
print(id(str3))
str13=tuple(string1)
print(str13)
print(id(str13))
print(id(1))
print(id(10))
x=10
print(x)



















