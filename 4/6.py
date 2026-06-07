
u=int(input("enter the number:"))
l=int(input("enter the number:"))
print("armstrong numbers between them are:")
for n in range(u,l+1):
   temp=n
   count=0
   sum=0
   while(temp>0):
      temp=temp//10
      count+=1
   temp=n
   while(temp>0):
      r=temp%10
      sum=sum+pow(r,count)
      temp=temp//10
      if(n==sum):
         print(n)
      
      
   