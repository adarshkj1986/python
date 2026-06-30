list=[1,2,3,3,4,4,4]
i=0
for j in range(1,len(list)):
    if list[j]!=list[i]:
        list[i+1]=list[j]
        i+=1
result=list[:i+1]
print(result)