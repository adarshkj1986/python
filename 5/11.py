bin=int(input("enter the number"))
count=0
while(bin>0):
    if(bin%2==1):
        count=count+1
    bin=bin//10
print("set bits are:",count)