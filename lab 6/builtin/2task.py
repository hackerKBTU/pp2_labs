text = input()
up=0
low=0
for i in text:
    if i.isupper():
        up +=1
    elif i.islower():
        low +=1
print("Uppercase letters: " ,up)
print("Lowercase letters:",low)