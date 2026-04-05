import os

filepath = os.getcwd()
fullpath = os.path.join(filepath, "CT08_08/sherlock.txt")

if not os.path.exists(fullpath):
    print("There is no such thing called sherlock.txt")

with open(fullpath, "r") as file:
    lines = file.read()
    print(lines)

print(f"Number of character in the text : {len(lines)}")

vowels = {
    "a" : 0,
    "e" : 0,
    "i" : 0,
    "o" : 0,
    "u" : 0
}

total_vowels = 0

for char in lines.lower():
    if char in vowels:
        vowels[char] += 1
        total_vowels += 1

print("\nVowel Counts:")
for v in vowels:
    print(f"{v} : {vowels[v]}")

print(f"Total vowels: {total_vowels}")

# Task 4: Calculate percentage
percentage = (total_vowels / len(lines)) * 100
print((f"Percentage of vowels: {percentage:.2f}%"))

# Task 5: Write results to a new file
output = open("vowel_counts.txt", "w")

output.write("Vowel Counts:")
for v in vowels:
    output.write("\n" + v + " : " + str(vowels[v]))

output.write("\nTotal vowels: " + str(total_vowels))
output.write("\nPercentage of vowels: {:.2f}%".format(percentage))

output.close()

print("\nResults saved to vowel_counts.txt successfully.")
