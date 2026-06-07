n=int(input("enter the number:"))
factor_n=0
for i in range(1,n):
    if(n%i==0):
        factor_n+=i
if(n==factor_n):
    print("perfect number")
else:
    print("not a perfect number")