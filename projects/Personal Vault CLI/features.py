import utils
import re

def add_note(username):

    data = utils.load_data()

    note_topic = input("Enter Note's Topic: ")
    note_content = input("Enter Note's Content: ")

    for entries in data:

        if entries.get("username") == username:

            new_note = {
                "topic": note_topic,
                "content": note_content
            }

            (entries["notes"]).append(new_note)
            utils.save_data(data)
            print("Note Added Successfully!")

def view_notes(username):

    data = utils.load_data()

    for entries in data:

        if entries.get("username") == username:

            if (number_of_notes := len(entries.get("notes"))) != 0: # if the notes list is not empty

                print(f"You have {number_of_notes} notes.\n")

                for note in entries.get("notes"):

                    print(f"Topic: {note["topic"]}")
                    print(f"Content: {note["content"]}\n")
                
                return
            
            else:

                print("You have no entries yet!")
                return
            
def search_notes(username):

    data = utils.load_data()

    for entries in data:

        if entries.get("username") == username:
            notes = entries.get("notes", [])
            
            if not notes:
                print("You have no notes!")
                return

            print("\n--- Search Notes ---")
            print("1. Custom search (keyword or regex)")
            print("2. Search Emails")
            print("3. Search Phone Numbers")
            print("4. Search IP Addresses")
            print("5. Search Dates")
            print("6. Search Money Values")
            
            choice = input("Choose an option: ").strip()

            if choice == "1":

                query = input("Enter search term/regex: ").strip()

                try:
                    pattern = re.compile(query, re.IGNORECASE)
                except re.error:
                    print("Invalid regex pattern!")
                    return
                
            elif choice == "2":
                pattern = re.compile(utils.email_pattern)

            elif choice == "3":
                pattern = re.compile(utils.phone_pattern)

            elif choice == "4":
                pattern = re.compile(utils.ip_pattern)

            elif choice == "5":
                pattern = re.compile(utils.date_pattern)

            elif choice == "6":
                pattern = re.compile(utils.money_pattern)
                
            else:
                print("Invalid choice!")
                return

            # Search logic
            found = False
            print(f"\nResults for your search:\n")
            
            for note in notes:
                topic = note.get("topic", "")
                content = note.get("content", "")
                
                if pattern.search(topic) or pattern.search(content):
                    found = True
                    print(f"Topic: {topic}")
                    print(f"Content: {content}\n")
            
            if not found:
                print("No matching notes found.")

            return

def delete_note(username):

    data = utils.load_data()

    for entries in data:

        if entries.get("username") == username:

            if (number_of_notes := len(entries.get("notes"))) != 0:

                print(f"You have {number_of_notes} notes.\n")

                for note in entries.get("notes"):

                    print(f"Topic: {note["topic"]}")
                    print(f"Content: {note["content"]}\n")
                
                user_note_delete = input("Enter the name of the note you want to delete: ")

                for note in entries.get("notes"):

                    if note.get("topic") == user_note_delete:

                        (entries["notes"]).remove(note)
                        utils.save_data(data)
                        print("Note deleted successfully!")
                        return
                
                print("Couldn't find the note!")
                return

            else:
                print("You have no notes!")

def edit_note(username):
    
    data = utils.load_data()

    for entries in data:

        if entries.get("username") == username:

            if (number_of_notes := len(entries.get("notes"))) != 0:

                print(f"You have {number_of_notes} notes.\n")

                for note in entries.get("notes"):

                    print(f"Topic: {note["topic"]}")
                    print(f"Content: {note["content"]}\n")
                
                user_note_edit = input("Enter the name of the note you want to edit: ")

                for note in entries.get("notes"):

                    if note.get("topic") == user_note_edit:

                        new_content = input("Enter the New Content: ")

                        note["content"] = new_content
                        utils.save_data(data)
                        print("Note Edited successfully!")
                        return
                
                print("Couldn't find the note!")
                return

            else:
                print("You have no notes!")