from datetime import datetime

def wish_me():

    current_hour = datetime.now().hour

    if current_hour < 12 and current_hour >= 0:
        greeting = "Good Morning"

    elif current_hour >=  12 and current_hour < 16:
        greeting = "Good Afternoon"

    elif current_hour < 23 and current_hour >= 16:
        greeting = "Good Evening"
    
    else:
        return f"Welcome back to Library Management System.\n"
    
    return f"{greeting}! Welcome back to Library Management System.\n"

def formatted_date_func():

    now = datetime.now()

    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_date

def get_valid_input(data_type, prompt):
    """function will return only when user enters a valid input"""

    while True:

        try: 

            user_input = data_type(input(prompt))
            return user_input

        except ValueError as e:

            print("Enter a valid input!")
            continue

def print_section_header(txt):

    to_print = "\n" + ("=" * 10) + txt + ("=" * 10) + "\n"

    print(to_print)

def print_section_footer(txt):

    to_print = "\n" + txt + "\n"

    print(to_print)