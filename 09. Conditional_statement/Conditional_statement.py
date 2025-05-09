#  ternary operator
a = 2
b = 330
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")

# if elif
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# if else ladder
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#  if single
if a > b: print("a is greater than b")

#  if with bitwise op
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


  a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


  a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


# ladder
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


#----------------------------------------------------------------
# while loop
i = 1
while i < 6:
  print(i)
  i += 1

  i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#----------------------------------------------------------------
# for each loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


for x in "banana":
  print(x)

# break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# pass
for x in [0, 1, 2]:
  pass

for x in range(6):
  print(x)

  for x in range(6):
   print(x)
else:
  print("Finally finished!")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

    adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

