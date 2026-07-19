from datetime import datetime
from enum import Enum

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |

     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """,
]

easy_words = [
    "apple",
    "bark",
    "camp",
    "desk",
    "frog",
    "glow",
    "jump",
    "lime",
    "mint",
    "neon",
    "park",
    "quiz",
    "rope",
    "surf",
    "wave",
]

medium_words = [
    "banana",
    "camera",
    "danger",
    "escape",
    "flight",
    "guitar",
    "honest",
    "jungle",
    "matrix",
    "nature",
    "planet",
    "shadow",
    "timber",
    "wizard",
    "zipper",
]

hard_words = [
    "astronaut",
    "blizzard",
    "cryptic",
    "duplicity",
    "eccentric",
    "galaxy",
    "hyphen",
    "infinite",
    "labyrinth",
    "mystify",
    "oxygen",
    "phantom",
    "rhythm",
    "unknown",
    "whisper",
]

tech_words = [
    "algorithm",
    "boolean",
    "compiler",
    "database",
    "function",
    "hardware",
    "internet",
    "keyboard",
    "network",
    "terminal",
]

def get_valid_input(data_type, prompt):
    """function will return only when user enters a non-empty valid input"""

    while True:
        # 1. Capture input and remove accidental leading/trailing spaces
        user_raw = input(prompt).strip()

        # 2. Block empty inputs or strings made entirely of spaces
        if not user_raw:
            print("Input cannot be empty!")
            continue

        try: 
            # 3. Cast to the desired data type
            return data_type(user_raw)

        except ValueError:
            print("Enter a valid input!")

class RoundType(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    BONUS = "bonus"

class PlayerAuthType(Enum):
    LOGIN = "login"
    SIGNUP = "signup"
    GUEST = "guest"

trolling = [
    "𐤃𐤌𐤁𐤎𐤎! What do you thought? Now guess either a letter or the entire word!",
    "𐤐𐤕𐤄𐤕𐤉𐤊! Wrong again. Pick another letter or guess the whole word!",
    "𐤄𐤋𐤐𐤋𐤎𐤎! Your luck is running out. Guess a letter or the full word now!",
    "𐤔𐤌𐤊𐤊! Not even close. Try a new letter or risk the whole word!",
]

"""
𐤃𐤌𐤁𐤎𐤎: Dumbass
𐤐𐤕𐤄𐤕𐤉𐤊: Pathetic
𐤄𐤋𐤐𐤋𐤎𐤎: Helpless
𐤔𐤌𐤊𐤊: Schmuck
"""

player_status = [
    "0 Mistakes: [ 🤍 🤍 🤍 🤍 🤍 🤍 ] (Healthy)",
    "1 Mistake:  [ 🔴 🤍 🤍 🤍 🤍 🤍 ] (Head)",
    "2 Mistakes: [ 🔴 🔴 🤍 🤍 🤍 🤍 ] (Torso)",
    "3 Mistakes: [ 🔴 🔴 🔴 🤍 🤍 🤍 ] (Left Arm)",
    "4 Mistakes: [ 🔴 🔴 🔴 🔴 🤍 🤍 ] (Right Arm)",
    "5 Mistakes: [ 🔴 🔴 🔴 🔴 🔴 🤍 ] (Left Leg)",
    "6 Mistakes: [ 💀 💀 💀 💀 💀 💀 ] (Game Over)"
]

def print_section_header(txt):

    to_print = "\n" + ("=" * 10) + f" {txt} " + ("=" * 10) + "\n"

    print(to_print)

def print_section_footer(txt):

    to_print = "\n" + txt + "\n"

    print(to_print)

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

def show_features():
    print("What do you want to do!")
    print("""
        1. Play New Game
        2. View Leaderboard
        3. View Rules
        4. Exit
    \n""")

def show_rules():
    """Displays the rules of the Hangman game."""
    print("""\n
╔══════════════════════════════════════════════════════════════╗
║                    HANGMAN - GAME RULES                      ║
╠══════════════════════════════════════════════════════════════╣
║ 1. There are four difficulty levels:                         ║
║    • Easy     (Common words)                                 ║
║    • Medium   (Moderate words)                               ║
║    • Hard     (Difficult words)                              ║
║    • Bonus    (Tech/Programming words)                       ║
║                                                              ║
║ 2. Standard Hangman rules:                                   ║
║    - Guess one letter at a time or the entire word.          ║
║    - You have 6 lives (wrong guesses).                       ║
║    - Correct letter reveals all occurrences.                 ║
║    - Wrong guess = lose 1 life.                              ║
║                                                              ║
║ 3. Points System:                                            ║
║    • Easy   → +5  points                                     ║
║    • Medium → +10 points                                     ║
║    • Hard   → +15 points                                     ║
║    • Bonus  → +25 points                                     ║
║                                                              ║
║ 4. Guest Mode: You can play only ONE round.                  ║
║    Your progress will NOT be saved.                          ║
║                                                              ║
║ Good luck and have fun!                                      ║
╚══════════════════════════════════════════════════════════════╝
\n""")

def show_difficulty():
    print("""\n
• Easy   → +5  points
• Medium → +10 points
• Hard   → +15 points
• Bonus  → +25 points
\n""")