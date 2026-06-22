text="hello"
vowels="aeiouAEIOU"
vowels_count=0
consonents_count=0
for char in text:
    if char.isalpha():
        if char in vowels:
            vowels_count+=1
        else:
            consonents_count+=1
print("vowels are:",vowels_count)
print("consonents are:",consonents_count)