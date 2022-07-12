#d={[1,2] : "jj"}
#print(d)#dic with key element as list will not taken because it is mutable

d={"kk" : [1,2]}
print(d)
d={"A" : "Apple", "a" : "Apple"} #dic with case sensitive
print(d)
d={"A" : "Apple", "A" : "Apple"} # dic cannot have two items with same key
print(d)
d={"A" : "Apple", "B" : "Bat"}#items can be added using key as index
d["C"]="Cat"
print(d)
d={"A" : "Ant", "B" : "Bat"}#items can be modified using key as index
d["B"]="Boll"
print(d)
#dictionary methods
d={1:"one"}
print(d)
d.clear()# clear the items in dictionary
print(d)

d={1:"one"}
print(d)
d.copy()# copy the items in dictionary
print(d)

d={1:"one",2:"two",3:"three"}
x=dict.fromkeys(d)
print(x)

d={'a':'ant','b':'bat','c':'cat'}
x=d.get('b')
print(x)

d={'a':'ant','b':'bat','c':'cat'}
x=d.items()
print(x)

d={'a':'ant','b':'bat','c':'cat'}
x=d.keys()
print(x)

d={'a':'ant','b':'bat','c':'cat'}
x=d.pop('b')
print(x)

d={'a':'ant','b':'bat','c':'cat'}
x=d.popitem()
print(x)

d={'a':'ant'}
x=d.setdefault('b','bat')
print(x)

d={'a':'ant','b':'bat'}
x={'c':'cat'}
print(x)
d.update(x)
print(d)


