arr1=[1,2,3,4,5,8,12]
count=0
count_2=0
for i in range(len(arr1)):
    if arr1[i]%2==0:
        count+=1
    elif arr1[i]%2!=0:
        count_2+=1
    else:
        print("invalid")
       
print("total even numbers are:",count)
print("total odd numbers are:",count_2)