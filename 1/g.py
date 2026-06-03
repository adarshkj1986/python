n=int(input("enter the number:"))
factor_sum=0
for i in range(1,n):
    if n%i==0:

     factor_sum=factor_sum+i
if(n==factor_sum):
    print("perfect no")
else:
    print("not a perfect no")