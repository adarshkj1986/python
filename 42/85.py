text="hello"
seen=[]
is_repeating=None
for char in text:
    if char in seen:
        is_repeating=char
    else:
        seen.append(char)
if is_repeating:
    print("the first repeating is:",is_repeating)
else:
    print("no repeating")