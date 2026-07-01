def binary(a,target):
    l=0
    r=len(a)-1
    while l<=r:
        middle=(l+r)//2
        if a[middle]==target:
           return middle
        elif a[middle]<target:
            l=middle+1
        else:
            r=middle-1
    return-1
a=[1,2,3,4]
print(binary(a,3))