def intersection_array(arr1,arr2):
    arr1.sort()
    arr2.sort()
    intersection=[]
    i,j=0,0
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr1[i]:
            j+=1
        else:
            if not intersection or intersection[-1]!=arr1[i]:
                intersection.append(arr1[i])
            i+=1
            j+=1
    return intersection
    
arr1=[1,2,3,4,5]
arr2=[2,5,6,7]
print("intersection is:",intersection_array(arr1,arr2))