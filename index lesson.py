import random
name=input("enter your name")
print(name[0])
length= len(name)
print(length)
position=random.randrange(0,length)
if position<=length:
    char =name[position]
    print(char)
else:
    print("thats out of range")
