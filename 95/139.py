a=[1,2,3,4]
b=[3,6,7,8,4]
common=[]
for i in a:
    if i in b and i not in common:
        common.append(i)
print(common)