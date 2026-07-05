import random
n=int(input("enter the number"))
target=random.randint(1,100)
while(n<101):
    if n==target:
        print("correct number guessed")
        break
    else:
        print("not correct number")
        break
