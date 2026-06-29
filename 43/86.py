n=[4,3,0,9,0,0,9,7]
j=1
for i in range(len(n)):
    if n[i]==0:
        j=i
        break
for i in range(j+1,len(n)):
    if n[i]!=0:
        n[i],n[j]=n[j],n[i]
        j+=1
print("the new list is:",n)