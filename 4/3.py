n=int(input("enter the number:"))
fib=[0,1]
for i in range(2,n):
   next_term=fib[-1]+fib[-2]
   fib.append(next_term)
print(fib)