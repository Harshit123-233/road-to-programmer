"""Day 06 of Learning Python. Today I've learnt:-
1. If... elif... else.
i. Shorthand If
ii. Logical Operators
iii. Nested If
iv. pass Statements
2. Match Statements
"""

a = 20
if a > 0:
    print("The number is positive.")
elif a < 0:
    print("The number is negative.")
elif a == 0:
    print("The number you entere is 0 which is neither positive nor negative.")
else:
    print("Error: Please Enter a valid number!")

#Shorthand if
a1 = 2
b1 = 330
print("A") if a1>b1 else print("B")

a2 = 10
b2 = 20
bigger = a2 if a2>b2 else b2
print("Bigger is", bigger)

username1 = ""
display_name = username1 if username1 else "Guest"
print("Welcome,", display_name)

a3 = 330
b3 = 330
print("A") if a3>b3 else print("=") if a3==b3 else print("B")

#Logical Operators
a4 = 200
b4 = 33
c4 = 500
if a4 > b4 and c4 > a4:
  print("Both conditions are True")

if a4 > b4 or a4 > c4:
  print("At least one of the conditions is True")

if not a4 > b4:
  print("a is NOT greater than b")

age = 25
is_student = False
has_discount_code = True
if (age<18 or age>65) and not is_student or has_discount_code:
   print("Discount Applies!")

#Nested if
username = "Emil"
password = "python123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")

score = 92
extra_credit = 5

if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")

#Python Pass Statement
age_check = 16

if age_check < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")


value_check = 50

if value_check < 0:
  print("Negative value")
elif value_check == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")

def calculate_discount(price):
  pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet

#Match Statements
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

month = 5
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")