text=input("enter the text:")
frequency={}
for char in text:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1
print("character frequency")
for char,count in frequency.items():
    print(f"{char}:{count}")