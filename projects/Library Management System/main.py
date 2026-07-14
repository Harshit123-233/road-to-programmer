from library_management import LibraryManager
import utils

def main():

    """The screen the user will see after logging in"""

    manager = LibraryManager()

    while True:

        utils.print_section_header("Library Management System")

        print("""Choose an option:
1. Books
2. Members
3. Exit                                       
                          
""")

        choice_menu = utils.get_valid_input(int, "Enter Your Choice: ")

        if choice_menu == 1:
            
            utils.print_section_header("Books")
            print("""
1. Add Book
2. Remove Book
3. Search Books
4. View All Books
5. Issue a Book
6. Return Book
7. Back
\n""")
            
            choice_submenu = utils.get_valid_input(int, "Enter your choice: ")

            if choice_submenu == 1:
                manager.add_books()

            elif choice_submenu == 2:
                manager.remove_books()

            elif choice_submenu == 3:
                manager.search_books()

            elif choice_submenu == 4:
                manager.view_books()

            elif choice_submenu == 5:
                manager.issue_book()

            elif choice_submenu == 6:
                manager.return_book()

            elif choice_submenu == 7:
                continue
            else:
                print("Invalid Input!")
                continue

        elif choice_menu == 2:
            print("\n","=" * 10,"Members","=" * 10)
            print("""
1. Register Member
2. Delete Member
3. View Members
4. Back
\n""")
            
            choice_submenu = utils.get_valid_input(int, "Enter your choice: ")

            if choice_submenu == 1:
                manager.register_member()

            elif choice_submenu == 2:
                manager.delete_member()

            elif choice_submenu == 3:
                db_data = manager.load_data(manager.members_path, "member")
                manager.view_member(db_data)

            elif choice_submenu == 4:
                continue
            
            else:
                print("Invalid Input!")
                continue

        elif choice_menu == 3:
            print("👋 Thanks for using Library Management System! Goodbye.")
            break

        else:
            print("Invalid option! Please choose 1-6.\n")

if __name__ == "__main__":

    """Requires Log In First"""

    utils.print_section_header("LOG IN")

    username = utils.get_valid_input(str, "Enter your username(should match the one on your ID card): ")
    password = utils.get_valid_input(str, "Password: ")

    if username == "harshit1234" and password == "SecretlySuperSaiyan": # change it as per yourself

        print(utils.wish_me())
        print("I know you have been assigned to look after the library. If it's your first day, then I want to let you know that we have a totally friendly environment for our not-so-hard-working employees. If it's not, then I don't need to lie to you. You've witnessed the truth but are too broke to reject this good-paying job!\n")

        main()

    else:

        print("The hell you doing over here trying to sneak in?! 🤬")


