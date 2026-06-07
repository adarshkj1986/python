n=int(input("enter the number:"))
a=0
b=1
if(n==1):
    print("0")
elif(n==2):
    print("1")
for i in range(n-2):
    next_term=a+b
    a=b
    b=next_term
print(b)