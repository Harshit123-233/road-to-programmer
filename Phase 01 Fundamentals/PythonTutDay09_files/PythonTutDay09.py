"""This is Day 09 of my Learning Python journey. Today I have learnt:-
1. Modules:-
i. create and use a module
ii. Naming and re-naming a module
iii. built-in modules
iv. Using the dir() function
v. Importing from module
"""

# built-in modules
import platform
from datetime import datetime

# self-created modules
import my_module as madagascar # just for the sake of example

madagascar.greeting("Harshit")

my_favorite_character = madagascar.anime1["name"]
print(f"My favorite Character is {my_favorite_character}.")

#Using the dir method
x = dir(platform)
y = dir(madagascar)

## Works for both built-in and self-created modules
print(x)
print(y)


# Using just an imported function from a module
now = datetime.now()

# Formatting it cleanly (Year-Month-Day Hour:Minute:Second)
# %Y = 4-digit year, %m = month, %d = day, %H = hour, %M = minute, %S = second
clean_time = now.strftime("%Y-%m-%d %H:%M:%S")

print(f"Current Date & Time: {clean_time}")