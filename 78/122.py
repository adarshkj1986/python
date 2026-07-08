bin=int(input("enter the number:"))
count=0
while(bin>0):
    if bin%10==1:
        count+=1
    bin=bin//10
print("total set bites are:",count)