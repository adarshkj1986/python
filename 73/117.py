n=[1,2,3,3,4,4,4]
i=0
for j in range(1,len(n)):
    if n[j]!=n[i]:
        n[i+1]=n[j]
        i+=1
result=n[:i+1]
print(result)