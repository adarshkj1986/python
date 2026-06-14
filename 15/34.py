def selection(a):
    n=len(a)
    for i in range(n):
        min_e=i
        for j in range(i+1,n):
            if a[j]<a[min_e]:
                min_e=j
        a[i],a[min_e]=a[min_e],a[i]
    return a
a=[5,4,2,6,1]
sorted_array=selection(a)
print("the sorted array is:",sorted_array)