n=[1,2,4,5]
sum=0
a=int(input("enter the number:"))
sum=a*(a+1)//2
sum_2=0
for i in range(0,len(n)):
    sum_2=sum_2+n[i]
    i+=1
missing_no=sum-sum_2
print("the missing no is:",missing_no)