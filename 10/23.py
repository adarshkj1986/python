string="hello world"
vowels="aeiouAEIOU"
vowel_count=0
consonent_count=0
for char in string:
    if char.isalpha():
        if char in vowels:
            vowel_count+=1
        else:
            consonent_count+=1
print("vowels are:",vowel_count)
print("consonants are:",consonent_count)
        