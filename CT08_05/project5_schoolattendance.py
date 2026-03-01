## Task 1: Create Student Database
# **Create the Initial Attendance Database​**

# - Create a dictionary to store the names of students and their attendance records.​
# - Initialize a dictionary where each key is a student’s name, and the value is a list of booleans representing attendance ​
# - (True for present, False for absent).​
# - This dictionary will serve as the database for all subsequent tasks.

students = {
    "sesko": [True, False, True],
    "fernandes": [False, False, True],
    "cunha": [True, True, True],
    # "casemiro": [True, False, False],
    # "mbeumo": [False, False, False],
    # "lammens": [False, True, False],
    # "dorgu": [False, True, True],
    # "mount": [True, True, False],
    # "dalot": [True, False, True],
    # "maguire": [True, True, True],
    # "shaw": [True, True, False],
    # "zirkzee": [False, True, False],
    # "Yoro": [True, False, True]

}

for student, past in students.items():
    print(student, past)
# ## Task 2: Take Student Attendance
# **Take Attendance​**

# Create a function called take_attendance()​

# Params:​
# - dictionary containing the student name and previous attendance​

# Function purpose:​
# - Loop through all the students, and ask if the student present or absence, and update the attendance accordingly.​
# - You must validate the input.​

# Return:​
# - updated dictionary with attendance record

def take_attendance(students_dict):
    for name in students_dict:
        attendance = input(f"Is {name} here? :").lower().strip()
        while attendance != "yes" and attendance != "no":
            print("answer yes or no")
            attendance = input(f"Is {name} here? :").lower().strip()


        if attendance == "yes":
            students_dict[name].append(True)
        else:
            students_dict[name].append(False)

# take_attendance(students)

# print(students)

## Task 3: Calculate Attendance Percentage
# **Create a function called attendance_percentage()​**

# Params:​
# - student: String – containing the student name​
# - attendance_dict: Dictionary – containing the class names and attendance​

# Function purpose:​
# - Lookup the student in the dictionary.​
# - Calculate the percentage of True values.​
# - Return the percentage of True values​

# Return:​
# - attendance_percentage: Float – containing the attendance percentage.


def attendance_percentage(student, attendance_dict):
    attendance_list = attendance_dict[student]
    sum_present = 0
    for status in attendance_list:
        if status:
            sum_present += 1
        
    return sum_present/len(attendance_list) * 100

# print(attendance_percentage("sesko", students))







def notify_low_attendance(attendance_dict, threshold):
    low_attendance_students = []
    for name in attendance_dict:
        attendance_percentage_student = attendance_percentage(name, attendance_dict)
        if attendance_percentage_student < threshold:
            low_attendance_students.append(name)
    return low_attendance_students

# print(notify_low_attendance(students, 50))


def view_attendance(students):
    for student in students:
        print(f"{student}: {students[student]}")





def menu():
#     print("""
# School Attendance System
# 1.
          
# """)
    while True:
        print("-----------------------------------------------------------------------------------------------------")
        print("Attendance System")
        print("0. View Attendance")
        print("1. Take Attendance")
        print("2. Calculate Attendance Percentage for a Student")
        print("3. Notify Low Attendance")
        print("4. Exit Program")
        choice = input("Enter your choice: ")

        while choice not in ("0", "1", "2", "3", "4"):
            print("Please enter only 0, 1, 2, 3 or 4")
            choice = input("Enter your choice: ")



        if choice == "0": 
            print(view_attendance(students))
        elif choice == "1":
            take_attendance(students)
        elif choice == "2":
            student_name = input("Enter the student's name: ").lower().strip()
            while student_name not in students:
                print("The student is not in this list")
                student_name = input("Enter the student's name: ").lower().strip()

            student_attendance_percentage = attendance_percentage(student_name, students)
            print(f"{student_name}'s attendance percentage: {student_attendance_percentage}")
        elif choice == "3":
            threshold = int(input("Enter the attendance threshold: "))
            print(notify_low_attendance(students, threshold))
        else:
            break

    

    
menu()