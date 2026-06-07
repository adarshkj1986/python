bin=int(input("enter the number:"))
dec,i=0,0
while(bin>0):
    r=bin%10
    exp=r*(2**i)
    dec=exp+dec
    bin=bin//10
    i+=1
print("the decimal no is:",dec)