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
        return f"Welcome back to your Expense Tracker.\n"
    
    return f"{greeting}! Welcome back to your Expense Tracker.\n"

def formatted_date_func():

    now = datetime.now()

    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_date

def get_valid_input(data_type, prompt):
    
    while True:

      try:
        
          user_input = data_type(input(prompt))

          return user_input

      except ValueError:
        
        print("Invalid Input!")
        continue
      
      



