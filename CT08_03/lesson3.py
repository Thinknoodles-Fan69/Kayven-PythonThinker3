### Learning 1 ###
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
    }

students["John"] = 56
students["Elias"] = 99
students["Kok Seng"] = 65

# print(f"Student Grades {students}")


### Challenge ###
# Try using an input() to ask which student you want to check the score for?
# What happens if you try accessing a student that does not exist?

# ask = input("Which students score do you want to check? :")
# if ask in students:
#     someones_grade = students[ask]
#     print(f"{ask}'s grade is {someones_grade}")
# else:
#     print("There is no student with that name")


### Lesson 3
students["Kok Seng"] = 75
# print(f"Student Grades {students}")

students["Alex"] = 98
# print(f"Student Grades {students}")

del students["Alex"]
# print(f"Student Grades {students}")

### Learning idk already ###

# for key, value in students.items():
#     print(f"{key}: {value}")  -One by one give the number and score

# for student in students:
#     print(student)  - Only give the name of the student in the students



### Task 1 ###

