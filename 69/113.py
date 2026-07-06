n="hello"
repeating=[]
for i in range(len(n)-1):
    if n[i]!=n[i+1]:
        repeating.append(n[i])
        break
    else:
        print("error")
print("the first non repeating is:",repeating)