#1
thislist = ["apple", "banana", "cherry"]
print(thislist)





#2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]

print(thislist)




#3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))





#4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)







#5
list1 = ["abc", 34, True, 40, "male"]

print(list1)



#6
mylist = ["apple", "banana", "cherry"]

print(type(mylist))




#7
thislist = list(("apple", "banana", "cherry"))
print(thislist)





#8
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])




#9
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])





#10
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])





#11
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])





#12
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])



#13
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")





#14
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)




#15
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#16
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)






#17
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)



#18
thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")

print(thislist) 






#19
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)



#20
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)



#21
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)



#22
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)

print(thislist) 




#23
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


#24
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)



#25
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)




#26
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)



#27
thislist = ["apple", "banana", "cherry"]
del thislist



#29
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#30
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


  #31
  thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


  #32
  thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


  #33
  thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]



#33
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)



#34
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)




#35
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)




#36
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)



#37
newlist = [x for x in range(10)]

print(newlist)




#38
newlist = [x for x in range(10) if x < 5]

print(newlist)



#39
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)




#40
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)




#41
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)





#42
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort(reverse = True)

print(thislist)






#43
thislist = [100, 50, 65, 82, 23]

thislist.sort(reverse = True)

print(thislist)







#44
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)





#45
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)



#46
thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)

print(thislist)






#47
thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.reverse()

print(thislist) 





#48
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)



#49
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)




#50
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)




#51
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)




#52
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)