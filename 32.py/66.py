text="hello everyone how are you all"
words=text.split()
is_longest=""
for word in words:
    if len(word)>len(is_longest):
        is_longest=word
print("longest word is:",is_longest)