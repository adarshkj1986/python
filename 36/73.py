def target_number(n,target):
    for i in range(len(n)):
        if n[i]==target:
            return i
            break
    return -1
n=[1,2,3,4,5,7,9]
target=int(input("enter the target number:"))
print(target_number(n,target))