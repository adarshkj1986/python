n=[1,2,2,3,3,3]
l_count=[]
max_count=0
for i in n:
    count=n.count(i)
    if count>max_count:
        l_count=i
        max_count=count
print("maximum occuring element is:",l_count)