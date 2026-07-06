st1="tea"
st2="ate"
if len(st1)!=len(st2):
    print("not anagram")
else:
    if sorted(st1)==sorted(st2):
        print("anagram")
    else:
        print("not anagram")
