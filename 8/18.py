def prime(n):
    for i in range(2,n):
        if(n%i==0):
            print("not a prime number")
            return
        else:
            print("prime number")
            return
prime(5)