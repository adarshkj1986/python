n=[1,2,2,2,3,3,4,5]
duplicate=set()
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if(n[i]==n[j]):
            duplicate.add(n[i])
print("the duplicates are:",duplicate)