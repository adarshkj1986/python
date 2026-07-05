sum=2000
while True:
    print("1. present balance")
    print("2. add money")
    print("3. withdraw money")
    print("4. present balance")
    print("5.exit")
    ch=int(input("enter the choices from(1-5):"))
    
    if ch==1:
        print("your present balance is:",sum)
    elif ch==2:
        add=int(input("enter your money:"))
        sum=sum+add
    elif ch==3:
        withdraw=int(input("enter the money to withdraw:"))
        sum=sum-withdraw
        if(withdraw>sum):
            print("not that much amount")
        else:
            print(sum)
    elif ch==4:
        print("your present balance is:",sum)
    elif ch==5:
        print("nothing")
        break
    else:
      print("invalid")