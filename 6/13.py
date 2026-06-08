arr=[1,2,3,3,4,4,4]
frequency={}
for i in arr:
    if  i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
for element in frequency:
    print(element,":",frequency[element])
