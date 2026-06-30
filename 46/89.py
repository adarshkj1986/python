list=[1,2,3,4]
target=int(input("enter the number:"))
sum=set()
for i in range(len(list)-1):
    if list[i]+list[i+1]==target:
        s=(list[i],list[i+1])
        sum.add(s)
        break
print("the pair is:",sum)