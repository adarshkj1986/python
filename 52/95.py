list=[5,4,2,6,1]
for i in range(len(list)):
    for j in range(0,len(list)-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print("the bubble sort is:",list)
