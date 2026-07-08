bin=int(input("enter the binary number:"))
dec,i=0,0
while(bin>0):
    r=bin%10
    exp=r*2**i
    dec=dec+exp
    bin=bin//10
    i+=1
print("binary to decimal:",dec)

