n="programming"
l_count=""
max_count=0
for char in n:
    count=n.count(char)
    if count>max_count:
        l_count=char
        max_count=count
print("maximum occurring character is:",l_count)