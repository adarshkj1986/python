a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
f_a=set()
f_b=set()
for i in range(1,a+1):
    if a%i==0:
        f_a.add(i)
for i in range(1,b+1):
    if b%i==0:
        f_b.add(i)
common_factor=f_a.intersection(f_b)
print("GCD is:",max(common_factor))