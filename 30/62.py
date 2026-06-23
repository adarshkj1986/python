string1=input("enter the string 1:")
string2=input("enter the string 2:")
st1=string1.replace(" ","").lower()
st2=string2.replace(" ","").lower()
if len(st1)!=len(st2):
    print("not anagram")
else:
    if sorted(st1)==sorted(st2):
        print("this is anagram")
    else:
        print("not anagram")