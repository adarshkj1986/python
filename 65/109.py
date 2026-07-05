def voting(n):
    if n>=18:
        print("eligible to vote")
    else:
        print("not eligible to vote")
    return n
n=int(input("enter the number"))
voting(n)