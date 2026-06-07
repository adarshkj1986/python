upper=int(input("enter the upper limit:"))
lower=int(input("enter the lower limit:"))
for n in range(upper,lower+1):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print("prime no are:",n)
