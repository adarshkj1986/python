arr=[1,3,7,5,8]
largest=arr[0]
for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]
second_largest=-1
for i in range(len(arr)):
    if arr[i]>second_largest and arr[i]!=largest:
        second_largest=arr[i]
print("the second largest is:",second_largest)