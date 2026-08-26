print("Adarsh Kumar Jha")
text = "hello world"

seen = set()
duplicates = set()

for char in text:
    if char in seen:
        duplicates.add(char)
    else:
        seen.add(char)

print("Duplicate characters:", list(duplicates))
#