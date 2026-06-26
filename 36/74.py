arr=[1,2,2,3,3,3,4,7,5,5]
frequency={}
for i in arr:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print("the frequency of the elements are:")
for i,count in frequency.items():
    print(f"{i}:{count}")
