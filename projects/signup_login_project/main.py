# Importing Necessary Modules. Oh sorry, my teacher has told me that comments should answer why, not what
import json
import os

db_path = 'D:\\Python Learning Files\\projects\\signup_login_project\\db_users.json'

def load_database():
    
    try:

        if not os.path.exists(db_path):

            with open(db_path, "w", encoding="utf-8") as file:
                json.dump([], file)

            return []

        with open(db_path, "r", encoding="utf-8") as file:

            return json.load(file)

    except json.JSONDecodeError:

        print(f"Warning: {db_path} was corrupted. Returning empty list.")
        return []

    except PermissionError:

        print(f"Error: Permission denied when accessing {db_path}.")
        return []

def user_login(data, user_name, pass_word):

    if any(user_name in d.values() for d in data):

        for credentials in data:

            if credentials.get("username") == user_name:

                if pass_word == credentials["password"]:

                    print("You have logged in Successfully!\n")
                    
                else:

                    print("You entered wrong password!\n")

            return
        
        print("An Error Occurred!\n")

    else:

        print("The username doesn't exist!\n")


while True:

    print("=======Sign Up or Log In=======")
    print("1. Sign Up [1]")
    print("2. Already a member, Log In [2]")
    print("3. Exit [3]")

    try:

        user_choice = int(input("What do you want to do?: "))

    except ValueError:

        print("Invalid Input! Please enter a number.\n")
        continue

    if user_choice == 1:

        data_from_db = load_database()

        username = input("Enter your username: ")

        if any(username in d.values() for d in data_from_db):

            print(f"{username} already exists! You may want to log in!\n")
            continue

        else:

            password = input("Enter your password: ")
            confirm_password = input("Confirm your password: ")

            if password != confirm_password :

                print("Passwords aren't matching, Boomer!\n")
                continue

            else:

                new_dict = dict(username = username, password = password)
                data_from_db.append(new_dict)
                data_from_db = json.dumps(data_from_db, indent = 4)

                try: 

                    with open(db_path, "w") as file:
                        file.write(data_from_db)
                    
                    print("You have signed up successfully!\n")
                
                except Exception as e:

                    print(f"An error occurred: {e} \n")
                    continue

    elif user_choice == 2:

        data_from_db = load_database()

        username = input("Enter your username: ")

        password = input("Enter your password: ")

        user_login(data = data_from_db, user_name = username, pass_word = password)

    elif user_choice == 3:
        
        print("Thanks for using the program!")
        break

    elif user_choice == 2191:

        print("Oh I see! You're the developer. Tf are you doing here?! Oh...\n")

    else:
        print("Are you stupid or some? Don't you see you have only three choices?\n")
