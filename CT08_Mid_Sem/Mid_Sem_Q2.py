"""
============================================================
Q2. Scrabble Game
============================================================
Write a PYTHON function that calculates the points
of a given word using a dictionary.

Requirements:
- Use a Python Dictionary for the letter points
- Ask for 5 words
- For each word, calculate the total score
- Print the score for each word in this format:
  Word #1:
  Score #1:

============================================================
"""

# ============================================================
# Step 1: Create the dictionary
# ============================================================

alphabet = {
"A":1,
"B":3,
"C":3,
"D":2,
"E":1,
"F":4,
"G":2,
"H":4,
"I":1,
"J":8,
"K":5,
"L":1,
"M":3,
"N":1,
"O":1,
"P":3,
"Q":10,
"R":1,
"S":1,
"T":1,
"U":1,
"V":4,
"W":4,
"X":4,
"Z":10
}

# ============================================================
# Step 2: Create a function calculate_score
# ============================================================
# - Loop through each letter in the word
# - Use the dictionary to find its value
# - Add up the total
# - Return the total score
# ============================================================

def calculate_score(alphabet):
    total = 0
    for letter, score in alphabet.items():
        total += score
    
    return total

print(f"Total score is {calculate_score(alphabet)}")

# ============================================================
# Step 3: Ask for 5 words
# ============================================================

words = []
for i in range(5):
    ask = input("Give me 5 words : ").lower().strip()
    words.append(ask)


# ============================================================
# Step 4: Print the score for each word in this format:
#         Word #1:
#         Score #1:
# ============================================================

scoring = 0
for i in range(len(words)):
    for letter, number in words.items():
        