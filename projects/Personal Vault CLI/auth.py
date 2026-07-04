import utils

def signup():

    data = utils.load_data()

    username = input("Username: ")
    password = input("Password: ")

    for entries in data:
        if entries.get("username") == username:
            print("Username already exists!")
            return

    new_entry = {
        "username": username,
        "password": password,
        "notes": []
    }

    data.append(new_entry)
    utils.save_data(data)
    print("New Account Created successfully!")

def login():
    data = utils.load_data()

    username = input("Username: ")
    password = input("Password: ")

    for entries in data:
        if entries.get("username") == username and entries.get("password") == password:
            print("Logged In Successfully!")
            return username
        
        
    print("Invalid Credentials!")
            