#1
a = 33
b = 200

if b > a:
  print("b is greater than a")


#2
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")





#3
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")





#4
a = 200
b = 33

if a > b: print("a is greater than b")



#5
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")




#6
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")




#7
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")








#8
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")



#9
a = 33
b = 200

if b > a:
  pass




#10
i = 1
while i < 6:
  print(i)
  i += 1



#11
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1




  #12
  i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)




#13
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")