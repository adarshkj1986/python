def rotate_array(a,k):
    n=len(a)
    if n==0:
        return a
    k=k%10
    return a[-k:]+a[:-k]
a=[6,7,8,9,10]
k=2
print("the rotated array to the left direction is:",rotate_array(a,k))