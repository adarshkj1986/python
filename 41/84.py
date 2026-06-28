n="hello"
result=None
for i in range(len(n)):
    r=False
    for j in range(len(n)):
        if i!=j and n[i]==n[j]:
            r=True
            break
    if not r:
        result=n[i]
        break
if result:
   print("the first non repeating is:",result)
else:
    print("nothing inside the string")
            