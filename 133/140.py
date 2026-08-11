text="Hello"
n=input("enter the character to be searched:")
count=0
for char in text:
    if char in n:
        count+=1
print("count is:",count)