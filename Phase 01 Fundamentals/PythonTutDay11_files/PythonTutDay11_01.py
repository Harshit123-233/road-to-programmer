"""Today is Day 11 of my Learning Python Journey. Today, I learnt:-
1. File Handling: Read (read(n), readline and looping through the lines of the file to be able to read the whole file, line by line), Write, Create and Delete"""

import os

my_path = "D:\\Python Learning Files\\Phase 01 Fundamentals\\PythonTutDay11_files\\file_handling_tut.txt"

#Creating a file
if os.path.exists(my_path): #checking if the file exists

    print("The file already exists!")

else:

    with open(my_path, "x"):

        print("The file has been created successfully!")

# Appending and overwriting the file

with open(my_path, "w") as my_file: #this will write the data in the file but if the file already has some data, then it will overwrite it. In that case we will use "a" instead of "w"
    my_file.write("My name is Harshit Kumar Singh. \n")
    my_file.write("I'm 19 years old, male and 6 feet tall. \n")
    my_file.write("My aim is to become a full-stack developer with useful skills who can bring a change into the world of programming and game development.")
    my_file.close()

# Reading a file
with open(my_path, "r") as my_file_read:
    my_file_read_data = my_file_read.read()
    print(my_file_read_data)

# Deleting a file
if os.path.exists(my_path):
    os.remove(my_path)
else:
    print("The file does not exist!")