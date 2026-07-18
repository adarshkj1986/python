text="rohit"
b="ram"
common=""
for char in text:
    if char in b and char!=common:
        common=common+char
print("the common is:",common)