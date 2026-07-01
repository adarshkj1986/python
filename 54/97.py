def linear(a,target):
    for i in range(len(a)):
        if a[i]==target:
            return i
    return -1
a=[1,2,3,4]
target=3
print("the index is:",linear(a,target))

