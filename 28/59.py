text="apple"
seen=[]
is_repeating=None
for char in text:
    if char in seen:
        is_repeating=char
        break
    else:
        seen.append(char)
if is_repeating:
    print("first repeating is:",is_repeating)
else:
    print("no one is repeating")