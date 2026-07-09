n="hebarllnoonsballoonsballoonsololsnab"
frequency={}
for char in n:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1
count_b=frequency.get("b",1)
count_a=frequency.get("a",1)
count_l=frequency.get("l",2)
count_o=frequency.get("o",2)
count_n=frequency.get("n",1)
count_s=frequency.get("s",1)
num_balloons=min(count_b,count_a,count_l,count_o,count_n,count_s)
print("no of times balloon appears:",num_balloons)