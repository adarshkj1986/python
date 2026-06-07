n=int(input("enter the number:"))
if n<2:
    print("not prime")
else:
    for i in range(2,n):
      if(n%i==0):
        print("not a prime number")
        break
    else:
        print(" this is prime number")