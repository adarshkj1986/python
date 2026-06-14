x=int(input("enter the number"))
bin=int(input("enter the number"))
ans=1
while(bin>0):
    if(bin%2==1):
       ans=ans*x
    x=x*x
    bin=bin//2
print("the power is:",ans)
