def left(a):
    n=len(a)
    if n==0:
        return a
    return a[k:]+a[:k]
k=2
a=[1,2,3,4]
print(left(a))