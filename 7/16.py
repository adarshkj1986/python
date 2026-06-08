x=int(input("enter the number:"))
n=int(input("enter the number"))
ans=1
while(n>0):
    if(n%2==1):
        ans=ans*x
    x=x*x
    n=n//2
print("the number is:",ans)