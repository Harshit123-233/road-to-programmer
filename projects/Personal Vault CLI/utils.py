import json
import os

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")

def load_data():

    try:
        if not os.path.exists(db_path):

            with open(db_path, "w", encoding="utf-8") as file:
                json.dump([], file)

            return []
        
        with open(db_path, "r", encoding="utf-8") as file:

            return json.load(file)
        
    except FileNotFoundError:
        return [] # Returns an empty list if database doesn't exists. The data structure is supposed to be: [{},{},...]
    
    except json.JSONDecodeError:
        print("Database file corrupted!")
        return [] # Returns an empty list if database file is corrupted.
    
    except PermissionError:

        print(f"Error: Permission denied when accessing 'data.json'.")
        return [] # Returns an empty list if the required permissions are not met

def save_data(data_to_save):

    data_to_save = json.dumps(data_to_save, indent = 4)

    with open(db_path, "w") as file:
        file.write(data_to_save)

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