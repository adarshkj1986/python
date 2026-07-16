n=int(input("enter the number"))
fibo=[0,1]
for i in range(2,n):
    next_term=f=fibo[-1]+fibo[-2]
    fibo.append(next_term)
print("the fibonacci series is:",fibo)