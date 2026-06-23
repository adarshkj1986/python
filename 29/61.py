n=int(input("enter the no"))
a=0
b=1
if n<=0:
   print("false")

elif n==1:
    print(a)
elif n==2:
    print(b)
else:
   for i in range(n-2):
     next_term=a+b
     a=b
     b=next_term
print(b)