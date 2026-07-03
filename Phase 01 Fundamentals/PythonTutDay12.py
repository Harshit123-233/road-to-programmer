"""This is Day 12 of my Learning Python Journey. Today I have learnt:-
1. RegEx
2. String Formatting: f-strings and .format()
3. None
4. User Input"""

# importing the RegEx module
import re

# I searched for this piece of text and made some edit for fun. The rest of the program is written by me
txt = """Hey heroes, here is the updated contact list for the Aura Leveling project. Please update the master CRM. 
For internal queries, contact Chuck Norris (Aura Manager) at chuck.norris@aura-leveling.com or via his office line +1 (555) 019-2834. His assistant, Goku, can be reached at goke_vegetalover@work-net.org or 555-123-4567. 
We also have external consultants on board. Dr. Bruce Lee (bruce.lee@kungfu.io) is available at +44 20 7946 0192, and John Claude Van Damme (john.van@aura.net) is at 1-800-555-0199 ext. 432. 
The development server is currently hosted at 192.168.1.105, but the staging environment has migrated to 10.0.0.42. 
Key deadlines to remember: 
- Requirements finalized by 2026-07-15 (Status: Approved)
- Alpha testing starts on 12/05/2026 (Status: Pending)
- Final deployment scheduled for 30-11-2026.
Budget allocations are as follows: Marketing got $15,000.50, Infrastructure was allocated $120,000, and R&D received $8,500.75. 
If you find any server errors like "Error 404: Not Found" or "Error 500: Internal Server Error", log them immediately. For emergency system rollbacks, ping admin-alerts@sys-backup.com.
"""

# Defining the Regex patterns
# Emails: Handles characters like dots, dashes, and underscores in names and domains
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Phone Numbers: Matches various lengths, country codes, brackets, and extensions
phone_pattern = r'\+?\d?[\s-]?\(?\d{3}\)?[\s-]?\d{3,4}[\s-]?\d{4}(?:\s*ext\.\s*\d+)?'

# IP Addresses: Looks for 1 to 3 digits separated by literal dots
ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

# Dates: Combines YYYY-MM-DD, MM/DD/YYYY, and DD-MM-YYYY formats using alternation (|)
date_pattern = r'\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b|\b\d{2}-\d{2}-\d{4}\b'

# Monetary Values: Looks for a literal $, numbers, commas, and optional decimals
money_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

# Extracting and displaying the data
print("--- EXTRACTED EMAILS ---")
emails = re.findall(email_pattern, txt)
print(emails)

print("\n--- EXTRACTED PHONE NUMBERS ---")
phones = re.findall(phone_pattern, txt)
print([p.strip() for p in phones]) # .strip() cleans up trailing whitespaces

print("\n--- EXTRACTED IP ADDRESSES ---")
ips = re.findall(ip_pattern, txt)
print(ips)

print("\n--- EXTRACTED DATES ---")
dates = re.findall(date_pattern, txt)
print(dates)

print("\n--- EXTRACTED MONETARY VALUES ---")
money = re.findall(money_pattern, txt)
print(money)

# STRING FORMATTING

user_name = input("\nEnter your name: ")
user_age = int(input("Enter your age in years: "))
user_bought = input("Enter the name of the item you bought: ")

user_bought_price = float(input("Enter the price of the product: "))
user_product_sold_price = float(input("Enter the amount you got after selling: "))

base_msg = f"So your name is {user_name} and you are {user_age} years old. You bought {user_bought} for {user_bought_price:.2f} and sold it for {user_product_sold_price:.2f}."

if user_bought_price < user_product_sold_price:
    profit = user_product_sold_price - user_bought_price
    
    try:
        profit_percentage = profit / user_bought_price
    except ZeroDivisionError:
        print("An error Occurred! Cannot divide by zero!")
        profit_percentage = 0

    print(f"{base_msg} Well that's a profit. You made a profit of {profit:.2f} and the profit percentage is {profit_percentage:.2%}.")

elif user_bought_price > user_product_sold_price:
    loss = user_bought_price - user_product_sold_price
    
    try:
        loss_percentage = loss / user_bought_price
    except ZeroDivisionError:
        print("An error Occurred! Cannot divide by zero!")
        loss_percentage = 0

    print(f"{base_msg} Well that's a loss. You made a loss of {loss:.2f} and the loss percentage is {loss_percentage:.2%}.")

else:
    business = "Break-Even"
    print(f"{base_msg} Well that's a {business}.")
