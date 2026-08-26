print("Adarsh Kumar Jha")
text="Python"
count=0
for v in text:
    if v not in "AEIOUaeiou":
        count+=1
print("consonents are:",count)
