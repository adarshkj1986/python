print("Adarsh Kumar Jha")
def find_first_duplicate(text):
  
    seen_characters = set()
   
    for char in text:
        
        if char in seen_characters:
            return char
        
       
        seen_characters.add(char)
        
  
    return None


sample_string = "abcdefcb"
result = find_first_duplicate(sample_string)

print("The first character to appear twice is:", result)
