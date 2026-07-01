list1=[1,2,3,4]
list2=[2,5,6]
common=[]
for i in list1:
    if i in list2 and i not in common:
        common.append(i)
print("the common elements are:",common)