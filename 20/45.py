n=int(input("enter the number"))
temp=n
count=0
sum=0
n1=n
while(temp>0):
    temp=temp//10
    count+=1
n=n1
while(n>0):
    r=n%10
    sum=sum+pow(r,count)
    n=n//10
if(n1==sum):
    print("this is a armstrong number")
else:
    print("not a armstrong number")