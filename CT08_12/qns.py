# Qns: Student Results File Processing

# You are given a text file called results.txt.
# Each line contains a student's name and mark, separated by a space.

# Example:
# Alex 92
# Ben 43
# Clara 78

# Your task:

# 1. Read the data from results.txt.

# 2. Convert the data into a dictionary called student_results.
#    The name should be the key.
#    The mark should be the value.


student_results = {}

with open("CT08_12/results.txt", "r") as file:
    for line in file:
        name, mark = line.strip().split()
        student_results[name] = int(mark)

print(student_results)

# 3. With the dictionary, create another dictionary that count the student in the follow range:
# 0 - 50, 51 - 70, 71 - 90, 91 - 100

# result_range = {
#     "0-50": 0,
#     "51-70": 0,
#     "71-90": 0,
#     "91-100": 0
# }

# for mark in student_results.values():
#     if mark > 74:
#         result_range["91-100"] += 1
#     elif mark > 70:
#         result_range["71-90"] += 1
#     elif mark > 50:
#         result_range["51-70"] += 1
#     elif mark > 0:
#         result_range["0-50"] += 1

# print(result_range)



result_range = {
    "0-50": [],
    "51-70": [],
    "71-90": [],
    "91-100": []
}

for name, mark in student_results.items():
    if mark > 90:
        result_range["91-100"].append(name)
    elif mark > 70:
        result_range["71-90"].append(name)
    elif mark > 50:
        result_range["51-70"].append(name)
    elif mark > 0:
        result_range["0-50"].append(name)

print(result_range)

# 4. Do a analysis of the score to get the following and print it to a output txt file 
# Min score: 
# Max Score:
# No of people in each range
# 0 - 50:  people
# 51 - 70: people
# 71 - 90: people
# 91 - 100: people
# the mode for range: __________
# average score:


min_score = min(mark)
max_score = max(mark)
average_score = sum(mark) / len(mark)
