n=int(input("enter the number"))
fib=[0,1]
for i in range(2,n):
    result=fib[-1]+fib[-2]
    fib.append(result)
print(fib)
