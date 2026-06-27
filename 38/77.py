def reverse(list):

    left=0
    right=len(list)-1
    while(left<right):
       list[left],list[right]=list[right],list[left]
       left+=1
       right-=1
    return list
list=[1,2,3,4]
print(reverse(list))
