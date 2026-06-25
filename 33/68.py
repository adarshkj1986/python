list=[1,2,2,3,4]
duplicate=set()

for i in range(len(list)):
    for j in range(i+1,len(list)):
      if list[i]==list[j]:
       duplicate.add(list[i])
print("duplicate value is:",duplicate)