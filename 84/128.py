def fibo(n):
    if n<=0:
        print([])
        return
    elif n==1:
        print([0])
        return
    fibo=[0,1]
    for i in range(2,n):
        n_t=fibo[i-1]+fibo[i-2]
        fibo.append(n_t)
    print(fibo)
fibo(5)