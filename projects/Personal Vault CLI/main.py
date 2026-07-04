import auth
import features

def main_menu(username):

    """The Vault menu after a successful login"""
    while True:

        print(f"\n--- {username}'s Personal Vault ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Edit Notes")
        print("6. Logout")

        try:
            user_choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid Input! Please Enter Again!")
            continue

        if user_choice == 1:
            features.add_note(username)
            continue

        elif user_choice == 2:
            features.view_notes(username)
            continue

        elif user_choice == 3:
            features.search_notes(username)
            continue

        elif user_choice == 4:
            features.delete_note(username)
            continue

        elif user_choice == 5:
            features.edit_note(username)
            continue

        elif user_choice == 6:
            print("Thanks for using Personal Vault!")
            print("Your secrets aren't secured with us :)")
            break

        else:
            print("Invalid Input!")

def welcome_screen():

    """The first screen a user sees"""
    while True:

        print("\n=== WELCOME TO PERSONAL VAULT ===")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        
        user_choice = input("Choose an option: ")
        
        if user_choice == "1":
            auth.signup()
            
        elif user_choice == "2":
            logged_in_user = auth.login()  # Captures the returned username

            if logged_in_user:  # If it's not None
                main_menu(logged_in_user)  # Hand the username to the vault menu
                
        elif user_choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid Input")

if __name__ == "__main__":

    welcome_screen()