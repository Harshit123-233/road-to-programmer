"""Today was Day 02 of learning Python and I learned:-
1. Python Strings:-
i. Quote inside quotes, multiline strings, strings are arrays, looping through a string, string length, checking string if present or not.
ii. Slicing
iii. Modify Strings
iv. Format Strings
v. Escape Characters
vi. String Methods"""

# Road To Programmer - Day 2
# Harshit, 19

name = "Harshit"

# 1. Basic operations
print(f"Name: {name}")
print(f"Length: {len(name)}")
print(f"First letter: {name[0]}")
print(f"Last letter: {name[-1]}")

# 2. Slicing
print(f"First 4 letters: {name[0:4]}")
print(f"Reverse: {name[::-1]}")

# 3. Checking & modifying
print("harshit" in name.lower())   # True

modified = name.replace("Harshit", "Harsh")
print(f"Modified: {modified}")

# 4. Formatting
age = 19
dream = "Master Python"
print(f"I am {age} years old and my dream is to {dream}.")

# 5. Multiline + Escape
bio = """I am a 19 year old guy
learning programming daily."""
print(bio)

# 6. String methods practice
text = "   Hello World!   "
print(text.strip().upper())