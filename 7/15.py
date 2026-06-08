n=input("enter the  elements:")
arr=list(map(int,n.split()))
d=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            found= False 
            for n in d:
              if n==arr[i]:
                 found= True
                 break
            if not found:
             d.append(arr[i])
print("duplicate value is:",d)