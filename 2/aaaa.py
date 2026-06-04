n=int(input("enter the number:"))
count=0
while(n>0):
    if(n%2==1):
        count=count+1
    n=n//10
print("set is:",count)