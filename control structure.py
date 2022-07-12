#if
a = 40
b = 300
if b > a:
  print("b is greater than a")
#elif
a = 55
b = 55
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#else
a = 55
b = 44
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else: 
    print(" b is lesser than a")
#while
    i = 1
while i < 10:  #1<10 prints upto 9
  print(i)
  i += 1
  #break
i = 1
while i < 10:
  print(i)
  if i == 5:
    break
  i += 1
#continue
i = 0
while i < 10:
  i += 1
  if i == 5:
    continue
  print(i)
#pass to avoid getting an error
  for x in [0, 1, 2]:
   pass
  #for loop

language = ["c", "python", "os"]
for x in language:
  if x == "python":
    break
  print(x)

language = ["c", "python", "os"]
for x in language:
  if x == "python":
    continue
  print(x)
  #range
  for x in range(2, 6):
   print(x)
for x in range(2, 30, 3): #increment the sequence with 3
  print(x)
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
