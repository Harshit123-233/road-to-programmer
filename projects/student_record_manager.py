"""=====STUDENT RECORD MANAGER====="""
import time
#I haven't learnt JSON yet. For now, this program wouldn't save the data once it's closed.
#Also, here I have assumed that roll number assigned to students aren't based on their names' aplhabetic order.

student_record = [] #this will be our database for now :)
#Also I was conflicted on whether to use dictionaries inside list or nested dictionaries.

#functions
def add_student():
    student_name = input("Enter the name of the student you want to add: ")

    if any(student_name in d.values() for d in student_record):

        print(f"{student_name} is already registered.")

    else:

        student_roll_number = int(input("Enter the student's roll number: "))

        if any(student_roll_number in a.values() for a in student_record):

            print("The Roll Number you entered is already assigned to someone else!")
        
        else:

            student_marks = int(input("Enter the student's marks: "))
            
            new_student_record = dict(name = student_name, roll_number = student_roll_number, marks = student_marks)

            student_record.append(new_student_record)
            print("Student's Details Added Successfully!","\n")

def view_all_students():

    if len(student_record) == 0:

        print("There are no students registered at this moment!")

    else: 

        print("Here's the Students Record:-")

        sorted_record = sorted(student_record, key=lambda x: x["marks"], reverse = True)
        
        for x in sorted_record:
            print(f"{(sorted_record.index(x)) + 1}. Name: {x["name"]} ; Roll Number: {x["roll_number"]} ; Marks: {x["marks"]}")
        
        print("\n")
    
def search_student():
    student_search_name = input("Enter the name of the Student you want to search about: ")
    sorted_record = sorted(student_record, key=lambda x: x["marks"], reverse = True)

    if any(student_search_name in d.values() for d in student_record):
        
        print(f"{student_search_name} is registered.")

        more_info = input("Do you want to know more about him? [Yes : y; No : n]")
        
        if more_info == "y":

            for student in sorted_record:

                if student.get("name").lower() == student_search_name.lower():

                    print(f"{student_search_name} scored {student["marks"]} marks.", "\n")

                    return
                
            print("An Error Occurred!", "\n")

        else:

            print("Okay!")
            print("\n")
                
    else:

        print(f"{student_search_name} is not registered!")

def update_marks():
    student_name_to_update = input("Enter the name of the student you want to update the marks for: ")

    for student in student_record:

        if student.get("name").lower() == student_name_to_update.lower():

            print(f"User's original marks is {student["marks"]}")
            new_marks = int(input("Enter new marks: "))

            if new_marks <= 200:
                
                student["marks"] = new_marks

                print(f"Updated: {student_name_to_update} scored {student["marks"]} marks.")
            
            else:

                print("Wrong Input!")

            return  # Stop searching and exit the function immediately

    
    print(f"Error: Student '{student_name_to_update}' not found in the records.")

def delete_student():

    print("What????? You want to delete the student! Just because he scored poorly 😱")
    time.sleep(2)
    print("Oh from the database ☺️")

    student_to_delete = input("Enter student's name: ")

    deleted = False

    # Loop over a copy of the list [:] to safely remove items in place
    for student in student_record[:]:
        if student.get("name") == student_to_delete:
            student_record.remove(student)
            deleted = True
            break

    if deleted:
        print(f"Successfully deleted {student_to_delete}. \n")
    else:
        print(f"Error: Student '{student_to_delete}' not found.")

def show_topper():

    if len(student_record) == 0:

        print("No one is registered at the moment!")
    
    else: 

        sorted_record = sorted(student_record, key=lambda x: x["marks"], reverse = True)
        topper_dict = sorted_record[0]

        print(f"The topper is {topper_dict["name"]} who has scored {topper_dict["marks"]} out of 200. Congratulations 🎉", "\n")

def summary_record():

    if len(student_record) == 0:

        print("No one is registered at the moment!")
    
    else: 
        print("""ITUS(Iski Topi Uske Sar) exam was conducted fairly and under the guidance of Chuck Norris on 31st of February 6769. Students appeared from all over Crunchyroll and participated enthusiastically. Aura-Farming was banned since Chuck Norris's aura was way too high!""")
        print("\n", "Following are the results of the exam:-")

        sorted_record = sorted(student_record, key=lambda x: x["marks"], reverse = True)
        
        all_marks_list = []
        for x in sorted_record:

            print(f"{(sorted_record.index(x)) + 1}. Name: {x["name"]} ; Roll Number: {x["roll_number"]} ; Marks: {x["marks"]}")

            all_marks_list.append(x["marks"])
        
        print("\n")

        average_marks = sum(all_marks_list) / len(all_marks_list)

        print(f"Average Marks: {average_marks}")
        print(f"Maximum Marks: {max(all_marks_list)}")
        print(f"Minimum Marks: {min(all_marks_list)}")
        print("\n")
    


while True:
    print("=======STUDENT RECORD MANAGER=======")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Summary")
    print("8. Exit", "\n")
    
    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        add_student()

    elif user_choice == 2:
        view_all_students()

    elif user_choice == 3:
        search_student()

    elif user_choice == 4:
        update_marks()

    elif user_choice == 5:
        delete_student()

    elif user_choice == 6:
        show_topper()

    elif user_choice == 7:
        summary_record()

    elif user_choice == 8:
        print("Thanks for using the Student Record Manager!")
        break

    else:
        print("Please enter a valid choice!", "\n")
