list=[1,2,3,4,5,4,4,4,6]
l_max=[]
count_max=0
for i in list:
    count=list.count(i)
    if count>count_max:
        l_max=i
        count_max=count
print("the maximum frequency element:",l_max)