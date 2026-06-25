n=input("enter the number")
arr1=list(map(int,n.split()))
n2=input("enter the number")
arr2=list(map(int,n2.split()))
merge=[]
i=0
j=0
while i<len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
        merge.append(arr1[i])
        i+=1
    else:
        merge.append(arr2[j])
        j+=1
while i<len(arr1):
    merge.append(arr1[i])
    i+=1
while j<len(arr2):
    merge.append(arr2[j])
    j+=1
print("the merge array is:",merge)


