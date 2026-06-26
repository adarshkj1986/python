arr=[2,5,6,10,9]
largest=arr[0]
for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]
print("the largest number is:",largest)