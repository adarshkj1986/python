text="programming"
seen=[]
is_repeating=None
for char in text:
    if char in seen:
        is_repeating=char
        break
    else:
        seen.append(char)
print("repeating is:",is_repeating)