a=[1,1,1,2,3,3]
max_l=[]
max_count=0
for i in a:
    count=a.count(i)
    if count>max_count:
        max_l=i
        max_count=count
print("the maximum occuring element is:",max_l)