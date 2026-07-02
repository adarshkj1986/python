n=int(input("enter the number:"))
count=0
while(n>0):
    r=n%10
    n=n//10
    count+=1
print("total digits are:",count)