n=int(input("enter the number"))
temp=n
n1=n
count=0
while(temp>0):
    temp=temp//10
    count=count+1
n=n1
sum=0
while(n>0):
    r=n%10
    sum=sum+pow(r,count)
    n=n//10
if(sum==n1):
    print("this is a armstrong number:")
else:
    print("not a armstrong number")