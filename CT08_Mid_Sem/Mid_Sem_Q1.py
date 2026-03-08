answer_key = ["A","B","B","A","A","C","C","A"]
student_ans = ["B","C","D","B","C","A","C","A"]

"""
============================================================
Q1. Quiz Auto-Marker
============================================================
You are building an auto-marker system for a multiple-choice quiz.
The program must compare a student's answers with the answer key.
It should calculate the score, identify which questions were wrong, and assign a grade.

- Write 3 functions:
    1) score_quiz(key, ans)
    2) wrong_questions(key, ans)
    3) grade(score, total)
- Do not change the function names or parameters.
- After writing your functions, uncomment the test code at the bottom to test.

============================================================
"""

# ============================================================
# Step 1: Write function score_quiz(key, ans)
# ============================================================
# - key and ans are lists of equal length
# - Compare answers at the same position
# - Return total number of correct answers
# ============================================================

def score_quiz(answer_key, student_ans):

    correct = 0
    for i in range(len(answer_key)):
        if student_ans[i] == answer_key[i]:
            correct += 1

    # print(correct)
    return correct
# print(f"Score = {score_quiz(answer_key, student_ans)}")


    

# ============================================================
# Step 2: Write function wrong_questions(key, ans)
# ============================================================
# - Return a list of question numbers (starting from 1) that are wrong
# - If all answers are correct, return an empty list
# ============================================================

def wrong_questions(answer_key, student_ans):
    wrongQ = []
    for i in range(len(answer_key)):
        if student_ans[i] != answer_key[i]:
            wrongQ.append(i + 1)
        
    # print(wrongQ)
    return wrongQ

# print(f"Wrong Question = {wrong_questions(answer_key, student_ans)}")


# ============================================================
# Step 3: Write function grade(score, total)
# ============================================================
# - Compute percentage = (score / total) * 100
# - Return:
#     "A" if percentage >= 80
#     "B" if percentage >= 70
#     "C" if percentage >= 60
#     "D" otherwise
# ============================================================

def grade(score, total):
    average = score / total * 100
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "D"

# grade(score_quiz(answer_key, student_ans), len(answer_key))

# ============================================================
# Step 4: Main Code Testing
# ============================================================
# Uncomment after writing your functions

# score = score_quiz(answer_key, student_ans)
# wrong = wrong_questions(answer_key, student_ans)
# final_grade = grade(score, len(answer_key))

# print("Score:", score)
# print("Wrong Questions:", wrong)
# print("Grade:", final_grade)

score = score_quiz(answer_key, student_ans)
wrong = wrong_questions(answer_key, student_ans)
final_grade = grade(score, len(answer_key))

print("Score:", score)
print("Wrong Questions:", wrong)
print("Grade:", final_grade)