text="hello"
str=""
max_count=0
for char in text:
    count=text.count(char)
    if count>max_count:
        str=char
        max_count=count
print(f"max occuring element is {str} it is occuring {max_count} times")