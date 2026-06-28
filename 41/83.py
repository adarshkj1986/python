n=input("enter the string:")
vowels="aeiuouAEIOU"
v_count=0
c_count=0
for char in n:
    if char.isalpha():
        if char in vowels:
            v_count+=1
        else:
            c_count+=1
print("total vowels are:",v_count)
print("total consonants are:",c_count)