text="PyTHon"
count_u=0
count_l=0
for char in text:
    if char.isupper():
        count_u+=1
    else:
        count_l+=1
print("upper case is:",count_u)
print("lower case is:",count_l)