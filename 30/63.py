text="programming"
max_char=""
max_count=0
for char in text:
    count=text.count(char)
    if count>max_count:
        max_count=count
        max_char=char
print("the maximum occurring character is:",max_char)