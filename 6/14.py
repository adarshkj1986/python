arr=input("enter the no of elements")
n=list(map(int,arr.split()))
print("array is:",n)
n.sort()
target=int(input("enter the number"))
def linear_search(n,target):
    for i in range(len(n)):
        if n[i]==target:
            return i
    return -1
print(linear_search(n,target))