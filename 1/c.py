a=int(input("enter the no"))
b=int(input("enter the no"))
factor_a=set()
for i in range(1,a+1):
    factor_a.add(i)
print()
factor_b=set()
for i in range(1,b+1):
    factor_b.add(i)
common_factor=factor_a.intersection(factor_b)
print("the gcd is:",max(common_factor))