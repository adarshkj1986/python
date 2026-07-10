def reverse(a):
    l=0
    r=len(a)-1
    while(l<r):
        a[l],a[r]=a[r],a[l]
        l+=1
        r-=1
    return a
a=[3,7,8,9]
print(reverse(a))