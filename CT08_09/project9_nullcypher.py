import os
import string


filepath = os.getcwd()
fullpath = os.path.join(filepath, "CT08_09/encrypted_note.txt")

if not os.path.exists(fullpath):
    print("ERROR: The encrypted note has vanished. Is someone trying to hide the truth?")

with open(fullpath, "r") as file:
    lines = file.read()
    print(lines)




clean_text = lines.lower()
for p in string.punctuation:
    clean_text = clean_text.replace(p, " ")
print(clean_text)


clean_text = clean_text.split()
result = ""

for word in clean_text:
    result += word[0]

print(result)




