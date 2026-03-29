import os

filepath = os.getcwd()
fullpath = os.path.join(filepath, "sherlock.txt")

if not os.path.exists(fullpath):
    print("There is no such thing called sherlock.txt")

with open(fullpath, "r") as file:
    lines = file.read()
    print(lines)

print(f"Number of character in the text : {len(lines)}")

vowels = {
    "a" : 0,
    "b" : 0,
    "c" : 0,
    "d" : 0,
    "e" : 0
}


