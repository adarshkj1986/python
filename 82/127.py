n=[2,7,11,15]
target=int(input("enter the number:"))
for i in range(len(n)-1):
    if n[i]+n[i+1]==target:
        list=[i,i+1]
       
print("the number is:",list)
