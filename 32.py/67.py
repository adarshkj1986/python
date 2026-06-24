text="programming"
result=""
for char in text:
    if char not in result:
        result+=char
print("removed duplicates value is:",result)