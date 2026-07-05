a=int(input("enter the number:"))
f_a=0
for i in range(1,a):
    if a%i==0:
        f_a+=i
if f_a==a:
    print("s")
else:
    print("n")