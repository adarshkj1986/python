#find all factors of a no
print("Adarsh Kumar Jha")
n=int(input("enter the no"))
factor=[]
for i in range(1,n+1):
    if n%i==0:
        factor.append(i)
print("the factors are:",factor)
