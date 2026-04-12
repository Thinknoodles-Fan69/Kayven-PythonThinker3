import random
user = {}


def generate_password(length=12):
    random_password = ""
    for i in range(length):
        random_password += chr(random.randint(33, 126))
        
    return random_password
    
def create_new_user(user):
    
    username = input("Create your own username: ")
    password = generate_password(length=12)
    print(f"Your password is:{password} ")
    user[username] = password


def update_password(user):
    name = input("What is your username: ")
    correctly_password = input("What is your currect password: ")
    if name in user:
        for name, password in user.items():
            if correctly_password == password:
                new_password = generate_password(length=12)
                print(f"Your new password is: {new_password}")
                user[name] = new_password
            else:
                print("Wrong Password Entered")
    else:
        print(f"There is no user with the username {name}")






def login(user):
    print("------Login------")
    correct_user = input("Enter your username: ")
    correct_password = input("Enter your password: ")
    if correct_user in user:
        for _, password in user.items():
            if correct_password == password:
                print("Welcome to the system")
            else: 
                print("Wrong password entered")

    else:
        print("Wrong username entered")




def view_user_data(user):
    print("----ADMIN-----")
    for player_user, player_password in user.items():
        encrypted_password = ""
        for _ in range(len(player_password)):
            encrypted_password += "*"
    
        print(f"Username:{player_user} Password:{encrypted_password}")







def view_menu():
    choice = input("""
        Username and Password Manager
        1. Create a New User
        2. Update Password
        3. Login
        4. View Stored Usernames and Passwords
        5. Exit
    
        Enter your option:
    """)

    return choice

while True:
    choice = view_menu()
    
    if choice == "1": 
        create_new_user(user)
    elif choice == "2":
        update_password(user)
    elif choice == "3":
        login(user)
    elif choice == "4":
        view_user_data(user)
    elif choice == "5":
        break