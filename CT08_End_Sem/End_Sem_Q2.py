import os
import string

filepath = os.getcwd()
fullpath = os.path.join(filepath, "CT08_End_Sem/review.txt")

if not os.path.exists(fullpath):
    print("There is no fullpath called review")

with open(fullpath, "r") as file:
    lines = file.readlines()
    # print(lines)

positive_word = "good"
negative_word = "bad"
positive = 0
negative = 0

characters = 0
for line in lines:
    clean_text = line.lower().strip()
    for p in string.punctuation:
        clean_text = clean_text.replace(p, " ")
    # print(clean_text)
    characters += len(clean_text)
    
# print(characters)



for line in lines:
    words = line.lower().split()
    for word in words:
        if word == "good":
            positive += 1
        elif word == "bad":
            negative += 1

good_percent = positive / len(lines) * 100

answer = ""
if good_percent > 70:
    answer += "postive"
elif good_percent > 40:
    answer += "mixed"
else: 
    answer += "negative"

output = open("CT08_End_Sem/review_result.txt", "w")
output.write("Review Text Analysis")
output.write("\n---------------")

output.write(f"\n Total Characters : {characters}")
output.write(f"\n Good reviews : {positive}")
output.write(f"\n Bad reviews : {negative}")
output.write(f"\n Percentage of good review : {good_percent}")
output.write(f"\n Overall rating : {answer}")













































