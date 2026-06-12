def binary(n,target):
    l=0
    r=len(n)-1
    while(l<=r):
        middle=l+r//2
        if(n[middle]==target):
            return middle
        elif(n[middle]<target):
            left=middle+1
        else:
            right=middle-1
n=[1,2,3,4,5]
target=3
result=binary(n,target)
print("the binary search is:",result)