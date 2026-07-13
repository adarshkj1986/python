n=input("enter the first list:")
a=list(map(int,n.split()))
v=input("enter the second list:")
b=list(map(int,v.split()))
print(a)
print(b)
sum=0
for i in range(len(a)):
    sum+=a[i]
print(sum)
sum_2=0
for i in range(len(b)):
    sum_2+=b[i]
print(sum_2)
sum_total=sum+sum_2
total=[int(digit) for digit in str(sum_total)]
print(total)
