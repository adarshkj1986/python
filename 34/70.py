st1="apple"
st2="mango"
common=""
for char in st1:
    if char in st2 and char not in common:
        common+=char
print("common characters are:",common)