from dataclasses import dataclass
from pathlib import Path
import utils
from datetime import datetime
import json

@dataclass
class Book:

    title: str
    author: str
    volume: float
    genre: str
    price: float
    availability: bool = True # tells if someone is currently borrowing it or not
    
    def books_to_dict(self):

        dict_books = dict(
            name = self.title,
            author = self.author,
            volume = self.volume,
            genre = self.genre,
            price = self.price,
            availability = self.availability            
        )

        return dict_books

@dataclass
class Member:

    name: str
    password: str
    books_borrowed: list
    membership_start: str
    membership_end: str

    def members_to_dict(self):

        dict_members = dict(
            name = self.name,
            password = self.password,
            books_borrowed = self.books_borrowed,
            membership_start = self.membership_start,
            membership_end = self.membership_end
        )

        return dict_members

class LibraryManager:

    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self):
        
        self.BASE_DIR = Path(__file__).resolve().parent
        db_dir = self.BASE_DIR / "database"
        db_dir.mkdir(parents=True, exist_ok=True)
        self.books_path = db_dir / "books.json"
        self.members_path = db_dir / "members.json"
        self.books = [] # contains books info as separate objects
        self.members = [] # contains members' info as separate objects

    

    def dicts_to_objects(self, list_cont_dicts, data_to_work_with: str):

        """Since I'm using 2 dataclasses, I can choose, which data to work with. Needs 2 parameters: list_cont_dicts & data_to_work_with (either book or member)"""

        sorted_db = sorted(list_cont_dicts, key=lambda x: (x.get("name") or "").lower()) # sorts the entries alphabetically and handles mixed-case sorting. Since both Books and Members has "name" key when as dicts, this shouldn't cause any error. Also, if somehow a "name" is None, then it handles that too.

        if data_to_work_with.lower().startswith("book"):

            self.books.clear()

            for book in sorted_db:

                new_object = Book(book["name"], book["author"], book["volume"], book["genre"], book["price"], book["availability"])

                self.books.append(new_object)

            return self.books
        
        self.members.clear()

        for member in sorted_db:

            new_object = Member(member["name"], member["password"], member["books_borrowed"], member["membership_start"], member["membership_end"])

            self.members.append(new_object)
        
        return self.members

    def load_data(self, data_path, data_to_work_with):

        try:

            if not data_path.exists():

                with open(data_path, "w", encoding = "utf-8") as file:

                    json.dump([], file)
                
                return []
            
            with open(data_path, "r", encoding = "utf-8") as file:


                data = json.load(file) #returns a list with expense entries inside as dictionaries

                return self.dicts_to_objects(data, data_to_work_with)
        
        except FileNotFoundError:

            return []
        
        except json.JSONDecodeError:

            print("Database File Corrupted!\n")
            return []

        except PermissionError:

            print(f"Error: Permission denied when accessing {data_path}.\n")
            return []
        
    def save_data(self, data_to_save, data_to_work_with: str):

        list_store_dict_temp = []

        if data_to_work_with.lower().startswith("book"):

            for book in data_to_save:

                list_store_dict_temp.append(book.books_to_dict())

            with open(self.books_path, "w", encoding = "utf-8") as file:
                json.dump(list_store_dict_temp, file, indent = 4)

            return
        
        for member in data_to_save:

            list_store_dict_temp.append(member.members_to_dict())
        
        with open(self.members_path, "w", encoding = "utf-8") as file:
                
            json.dump(list_store_dict_temp, file, indent = 4)

    def add_books(self):

        data_db = self.load_data(self.books_path, "book")

        utils.print_section_header("Add Book")

        new_book_title = utils.get_valid_input(str, "Book's Title: ") # I realized if I'm adding the book through this function then it's impossible to get None as book's name because that will be NoneType and since I've specified it be str, the function will not return unless users enters a valid string
        new_book_author = utils.get_valid_input(str, "Book's Author: ")
        new_book_volume = utils.get_valid_input(float, "Volume: ")
        new_book_genre = utils.get_valid_input(str, "Genre: ")
        new_book_price = utils.get_valid_input(float, "Price: ")
        new_book_availability = True

        # I'm assuming that we have only one copy/piece of a book. In the next version I'll add the "pieces_available" too!

        new_book = Book(new_book_title, new_book_author, new_book_volume, new_book_genre, new_book_price, new_book_availability)

        data_db.append(new_book)

        self.save_data(data_db, "book")

        utils.print_section_footer("Book Added Successfully!")
        
    def _view_books_by_name(self, db_data):

        for index, book in enumerate(db_data, start = 1):
            print(f"{index}. {book.title} - {book.volume} - {book.author} - {book.genre}")

    def _view_books_by_author(self, db_data): 

        author_books = {}
    
        for book in db_data:
            author = book.author
            if author not in author_books:
                author_books[author] = []
            author_books[author].append(book)

        for index, (author, books) in enumerate(author_books.items(), start=1):
            print(f"{index}. {author}:-")
            for second_index, each_value in enumerate(books, start=1):
                status = "Available" if each_value.availability else "Unavailable"
                print(f"\t{second_index}. {each_value.title} - {each_value.genre} - {status}")
            
            print("\n")

    def _view_books_by_genre(self, db_data):

        genre_books = {}

        for book in db_data:
            genre = book.genre
            if genre not in genre_books:
                genre_books[genre] = []
            genre_books[genre].append(book)
        
        for index, (genre, books) in enumerate(genre_books.items(), start=1):
            print(f"{index}. {genre}:-")
            for second_index, each_value in enumerate(books, start=1):
                status = "Available" if each_value.availability else "Unavailable"
                print(f"\t{second_index}. {each_value.title} - {each_value.author} - {status}")
            
            print("\n")

    def _view_books_by_availability(self, db_data):

        available_books_list = []
        not_available_books_list = []
        
        for books_to_view in db_data:

            if not books_to_view.availability :

                not_available_books_list.append(books_to_view)
                continue

            available_books_list.append(books_to_view)
        
        print("\n Books Available:-")

        for index, available_books in enumerate(available_books_list, start = 1):

            print(f"{index}. {available_books.title} - {available_books.author} - {available_books.genre}")
        
        if len(not_available_books_list) != 0:

            print("\n Books Issued/Unavailable:-")
            for index, not_available_books in enumerate(not_available_books_list, start = 1):

                print(f"{index}. {not_available_books.title} - {not_available_books.author} - {not_available_books.genre}")

            utils.print_section_footer("That's all we have for now!")

            return

        utils.print_section_footer("That's all we have for now!")

    def view_books(self):

        while True:
            db_data = self.load_data(self.books_path, "book")
            utils.print_section_header("View Books")
            print("""
        1. By Name
        2. By Author
        3. By Genre
        4. By Availability
        5. Back                  
            """)

            choice = utils.get_valid_input(int, "Enter how you want to view books: ")

            if choice == 1:
                self._view_books_by_name(db_data)
            elif choice == 2:
                self._view_books_by_author(db_data)
            elif choice == 3:
                self._view_books_by_genre(db_data)
            elif choice == 4:
                self._view_books_by_availability(db_data)
            elif choice == 5:
                break
            else:
                print("Invalid Input!")

    def remove_books(self):

        utils.print_section_header("Remove Book")

        print("""
        1. Individual
        2. Genre
        3. Author
        4. Back           
        """)

        how_to_delete = utils.get_valid_input(int, "How do you want to Delete: ")

        if how_to_delete == 1:

            db_data = self.load_data(self.books_path, "book")
            self._view_books_by_name(db_data)
            
            while True: 
                print("\n")
                choice = utils.get_valid_input(int, "Enter the index of the book you want to Delete: ")

                index_to_delete = choice - 1

                if 0 <= index_to_delete < len(db_data): 
                    removed_item = db_data.pop(index_to_delete)
                    self.save_data(db_data, "book")
                    print(f"Successfully deleted book: {removed_item.title} - {removed_item.author}\n")

                    delete_more = utils.get_valid_input(str, "Do you want to delete more? [y/n]: ").lower()

                    if delete_more == "y":
                        # Reload and show updated list
                        db_data = self.load_data(self.books_path, "book")
                        self._view_books_by_name(db_data)
                        continue
                    elif delete_more == "n":
                        break
                    else:
                        print("Invalid Input!")
                else:
                    print("Error: Index number out of range!\n")
        
        elif how_to_delete == 2:  # Genre
            db_data = self.load_data(self.books_path, "book")
            self._view_books_by_genre(db_data)

            genre_to_delete = utils.get_valid_input(str, "Enter the Genre: ").strip().lower()
            deleted_books = []
            i = 0
            while i < len(db_data):
                if db_data[i].genre.strip().lower() == genre_to_delete:
                    deleted_books.append(db_data.pop(i))
                else:
                    i += 1

            self.save_data(db_data, "book")

            utils.print_section_header("Deleted Books")
            for index, deleted_book in enumerate(deleted_books, start=1):
                print(f"{index}. {deleted_book.title}")
            utils.print_section_footer("Deleted Successfully!")

        elif how_to_delete == 3:  # Author
            db_data = self.load_data(self.books_path, "book")
            self._view_books_by_author(db_data)

            author_to_delete = utils.get_valid_input(str, "Enter the Author: ").strip().lower()
            deleted_books = []
            i = 0
            while i < len(db_data):
                if db_data[i].author.strip().lower() == author_to_delete:
                    deleted_books.append(db_data.pop(i))
                else:
                    i += 1

            self.save_data(db_data, "book")

            utils.print_section_header("Deleted Books")
            for index, deleted_book in enumerate(deleted_books, start=1):
                print(f"{index}. {deleted_book.title}")
            utils.print_section_footer("Deleted Successfully!")
            
        elif how_to_delete == 4:
            return
        else:
            print("Invalid Input!")
            return

    def search_books(self):

        db_data = self.load_data(self.books_path, "book")

        book_to_search = utils.get_valid_input(str, "Enter the Book's name: ")

        for index, book in enumerate(db_data, start = 1):

            if book_to_search.lower() == (book.title).lower():

                print("Found a match!")
                
                found_or_not = utils.get_valid_input(str, f"Is it {index}. {book.title} written by {book.author}? [y/n]: ")

                if found_or_not == "y":

                    print("I'm happy you found the book!")
                    return

                else:

                    print("I'm sorry! Finding a new match!")
                    continue

        print("I'm sorry! Looks like the book you're searching for, isn't available!")

    
    def register_member(self):

        utils.print_section_header("Register Member")

        new_member_name = utils.get_valid_input(str, "Name: ")
        new_member_password = utils.get_valid_input(str, "Password: ")
        confirm_password = utils.get_valid_input(str, "Confirm Password: ")

        if new_member_password != confirm_password:

            print("Passwords Should Match!")
            return
        
        new_member_books_borrowed = []

        new_member_membership_start = utils.get_valid_input(str, "Membership Starts[MM YYYY]: ")

        try:
            start_date_obj = datetime.strptime(new_member_membership_start, "%m %Y")
            end_date_obj = start_date_obj.replace(year=start_date_obj.year + 1)
            new_member_membership_end = end_date_obj.strftime("%m %Y")
        except ValueError:
            print("Invalid date format! Use MM YYYY (e.g. 07 2026)")
            return

        new_member = Member(new_member_name, new_member_password, new_member_books_borrowed, new_member_membership_start, new_member_membership_end)

        db_data = self.load_data(self.members_path, "member")
        db_data.append(new_member)

        self.save_data(db_data, "member")
        utils.print_section_footer("Member Registered Successfully!")

    def view_member(self, data):

        utils.print_section_header("Members")

        for index, member in enumerate(data, start = 1):

            month_start, year_start = member.membership_start.split()
            month_end, year_end = member.membership_end.split()

            membership_start_display = f"{month_start}/{year_start}"
            membership_end_display = f"{month_end}/{year_end}"

            print(f"{index}. Name: {member.name}, Membership: {membership_start_display} - {membership_end_display}\n")

        utils.print_section_footer("That's all!")


    def delete_member(self):

        db_data = self.load_data(self.members_path, "member")

        self.view_member(db_data)

        utils.print_section_header("Delete Member")

        choice = utils.get_valid_input(int, "Enter the member to delete: ")

        index_to_delete = choice - 1

        if 0 <= index_to_delete < len(db_data):

            utils.print_section_footer("Enter credentials to confirm!")

            member_to_delete_name = utils.get_valid_input(str, "Name: ")
            member_to_delete_password = utils.get_valid_input(str, "Password: ")

            if (db_data[index_to_delete]).name == member_to_delete_name and (db_data[index_to_delete]).password == member_to_delete_password:

                if len(db_data[index_to_delete].books_borrowed) == 0:

                    removed_member = db_data.pop(index_to_delete)
                    self.save_data(db_data, "member")
                    print(f"Successfully Removed {removed_member.name}.\n")
                    return
                
                print(f"The member hasn't returned the books yet! Couldn't Delete the member!\n")

            else:
                print("Incorrect Credentials!\n")
                return
        
        else:
            print("Index out of range!\n")
            return

    def issue_book(self):
        db_data_books = self.load_data(self.books_path, "book")
        db_data_members = self.load_data(self.members_path, "member")

        utils.print_section_footer("Only Members are allowed to issue a book!")

        issuer_name = utils.get_valid_input(str, "Name: ")
        issuer_password = utils.get_valid_input(str, "Password: ")

        for member in db_data_members:
            if member.name.lower() == issuer_name.lower() and member.password == issuer_password:
                if len(member.books_borrowed) != 0:
                    print("You already have a book to return!")
                    print(f"Book: {member.books_borrowed[0]['name'] if member.books_borrowed else 'None'}\n")
                    return

                print("You're eligible for issuing books!")
                print("Don't forget only one book at a time!\n")

                book_to_issue = utils.get_valid_input(str, "Book's Name: ")

                for book in db_data_books:
                    if book_to_issue.lower() == book.title.lower():
                        if book.availability:
                            print(f"Yes! You can borrow {book.title}!")
                            member.books_borrowed.append(book.books_to_dict())
                            book.availability = False
                            self.save_data(db_data_members, "member")
                            self.save_data(db_data_books, "book")
                            utils.print_section_footer("You have successfully issued the book!")
                            return
                        else:
                            print(f"I'm sorry! {book.title} is currently unavailable!\n")
                            return

                print(f"We don't have '{book_to_issue}'!\n")
                return

        print("Invalid Credentials!\n")


    def return_book(self):
        db_data_books = self.load_data(self.books_path, "book")
        db_data_members = self.load_data(self.members_path, "member")

        issuer_name = utils.get_valid_input(str, "Name: ")
        issuer_password = utils.get_valid_input(str, "Password: ")

        for member in db_data_members:
            if member.name.lower() == issuer_name.lower() and member.password == issuer_password:
                if len(member.books_borrowed) == 0:
                    print("You have no pending returns!")
                    return

                borrowed = member.books_borrowed[0]
                print(f"Returning book: {borrowed.get('name', 'Unknown')}\n")

                # Mark book as available
                for book in db_data_books:
                    if borrowed.get('name') == book.title:
                        book.availability = True
                        break

                member.books_borrowed.clear()
                self.save_data(db_data_members, "member")
                self.save_data(db_data_books, "book")

                utils.print_section_footer("Thanks for returning the book!")
                return

        print("Invalid Credentials!\n")