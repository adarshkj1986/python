n=int(input("enter the number:"))
temp=n
sum=0
while(temp>0):
    digit=temp%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    sum+=fact
    temp=temp//10
if sum==n:
    print("this is a strong number")
else:
    print("this is not a strong number")
