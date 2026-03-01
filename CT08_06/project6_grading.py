# Predefined data
answer_key = ["A", "B", "B", "D"]  # Correct answers for the quiz
student_answers = {
    "john": ["A", "C", "B", "D"],
    "jane": ["A", "B", "B", "D"],
    "alice": ["A", "C", "C", "D"],
    "bob": ["A", "B", "B", "D"]
}

def grade_all_students(student_answers, answer_key):
    quiz_scores = {}
    for name, answer in student_answers.items():
        temp_score = 0
        for i in range(len(answer_key)):
            if answer[i] == answer_key[i]:
                temp_score += 1
        
        quiz_scores[name] = temp_score/len(answer_key) * 100
    return quiz_scores
quiz_scores = grade_all_students(student_answers, answer_key)
# print(quiz_scores)
        


def calculate_average_score(quiz_scores):
    sum = 0
    for _, score in quiz_scores.items():
        sum += score
    return sum/ len(quiz_scores)
average = calculate_average_score(quiz_scores)
# print(average)



def find_highest_scorer(quiz_scores):
    highest_scorer = []
    max_score = 0
    for _, score in quiz_scores.items():
        if score > max_score:
            max_score = score

    for name, score in quiz_scores.items():
        if score == max_score:
            highest_scorer.append(name)
    
    return highest_scorer
# print(find_highest_scorer(quiz_scores))
        

def display_results(quiz_scores):
    for name, score in quiz_scores.items():
        print(f"{name} has a score of {score}")

# display_results(quiz_scores)


def menu():

    while True:
        print("-----------------------------------------------------------------------------------------------------")
        print("Grading System")
        print("1. View Grades For All Students")
        print("2. Calculate Average Score")
        print("3. Find Highest Scorer")
        print("4. Display Results")
        print("5. Exit Program")
        choice = input("Enter your choice: ")

        while choice not in ("1", "2", "3", "4", "5"):
            print("Please enter only 1, 2, 3, 4, 5")
            choice = input("Enter your choice: ")



        if choice == "1": 
            print(quiz_scores)
        elif choice == "2":
            print(average)
        elif choice == "3":
            print(find_highest_scorer(quiz_scores))
        elif choice == "4":
            display_results(quiz_scores)
        else:
            break


menu()