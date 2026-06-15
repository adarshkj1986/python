def reverse(a):
    l=0
    r=len(a)-1
    while(l<=r):
        a[l],a[r]=a[r],a[l]
        return a
a=[1,2,3]
print("reverse is:",reverse(a))