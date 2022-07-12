line1="we are in python session"   #equality operator ==
line2="we are in python session"
if line1==line2:
    print("same")
else:
    print("different")
#built-in string method
line1="we are in python session"   
line2="we are in py session"
if line1 in line2:
    print("same")
else:
    print("different")   
#find()and index()
line1="we are in python session"
line2="python"
print(line1.find(line2))
line1="we are in python session"
line2="python"
print(line1.index(line2))
    
#import re.compile
import re
text_to_search="abcdefghijklmnopqrstuvwxyz"
pattern=re.compile(r'abc') #raw data
res=re.match(pattern,text_to_search)
print(res)
print(type(pattern))
print(pattern)
#re.match()
import re
text_to_search="abcdefghijklmnopqrstuvwxyz"
pattern=re.compile(r'abc') #raw data
res=re.match(pattern,text_to_search)
print(res)
res=re.match(pattern,text_to_search)
print(pattern)
#re.search
import re
text_to_search="abcdefghijklabcmnopqrstuvwxyz"
pattern=re.compile(r'abc') #raw data
res=re.match(pattern,text_to_search)
print(res)
res=re.search(pattern,text_to_search)
print(res)
res=re.findall(pattern,text_to_search)#find all
print(res)
#re.fullmatch
text_to_search="abcdefghijklabcmnopqrstuvwxyz"
text="abc"
pattern=re.compile(r'abc') #raw data
res=re.match(pattern,text_to_search)
print(res)
res=re.search(pattern,text_to_search)
print(res)
res=re.findall(pattern,text_to_search)#find all
print(res)
res=re.fullmatch(pattern,text)
print(res)
import re
text_to_search="abcdefghijklabcmnopqrstuvwxyz"
text="abc"
pattern=re.compile(r'abc') #raw data
res=re.match(pattern,text_to_search)
print(res)
res=re.search(pattern,text_to_search)
print(res)
res=re.findall(pattern,text_to_search)#find all
print(res)
res=re.fullmatch('abc',text,flags=re.IGNORECASE)
print(res)
#re.finder()
import re
text_to_search="abcdefghijklabcmnopqrstuvwxyz"
pattern=re.compile(r'abc') #raw data
res=re.finditer(pattern,text_to_search)
for result in res:
    print(res)
#re.sub()
import re 
text_to_search="abcdefghijklabcmnopqrstuvwxyz"
pattern=re.compile(r'abc') #raw data
res=re.sub(pattern,'xyz',text_to_search)
print("sub:",res)
#re.subn()
import re 
text_to_search="abcdefghijklabcmnopqrstuvwxyz"
pattern=re.compile(r'123') 
res=re.subn(pattern,'xyz',text_to_search)
print("subn:",res)
'''#group()
import re
string='39801 356 2101 1111'
pattern='(\d{3}(\d{2})'
match=res.search(pattern,string)
if match:
    print(match.group)
else:
    print("pattern not found")'''
#re.escape()
import re
print(re.escape("Hello 123 .?!@ world"))
#start90 end() span()
import re
string='39801 356 2102 1111'
pattern='(\d{3})(\d{2})'
match=re.search(pattern,string)
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
else:
    print("pattern not found")
    #re.split()
import re 
text_to_search="abcdefghijklabcmnopqrstuvwxyz"
pattern=re.compile(r'abc') 
res=re.split(pattern,text_to_search)
print("split",res)  
    
    
    
