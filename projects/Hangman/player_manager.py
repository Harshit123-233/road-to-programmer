from pathlib import Path
from dataclasses import dataclass
import json
import utils

@dataclass
class Player:
    name: str
    password: str
    score: int = 0

    def to_dict(self):

        return {
            "name": self.name,
            "password": self.password,
            "score": self.score
        }
    
    @classmethod
    def to_object(cls, entry: dict):

        return cls(
            entry["name"],
            entry["password"],
            entry.get("score", 0)
        )

class PlayerManager:
    """Manages user log in, leaderboard and other related tasks"""

    def __init__(self):
        
        self.BASE_DIR = Path(__file__).resolve().parent
        db_dir = self.BASE_DIR / "database"
        db_dir.mkdir(parents=True, exist_ok=True)
        self.data_path = db_dir / "data.json"

        self.player_data = []

    def load_data(self) -> list[Player]:
        """Loads player's data from data file and returns a list with Player objects inside"""
        
        try:
            
            if not self.data_path.exists():
                with open(self.data_path, "w", encoding = "utf-8") as file:
                    json.dump([], file)
                self.player_data.clear()
                return []
            
            with open(self.data_path, "r", encoding = "utf-8") as file:
                data_from_db = json.load(file) # a list
                self.player_data.clear()
                for data in data_from_db:
                    self.player_data.append(Player.to_object(data))
                return self.player_data
            
        except (json.JSONDecodeError, FileNotFoundError, PermissionError) as e:
            print(f"Error loading data: {type(e).__name__} - {e}")
            self.player_data.clear()
            return []
    
    def save_data(self, data_to_save: list[Player]) -> None:
        """Saves data to the data file."""

        temporary_list = []

        for data in data_to_save:
            temporary_list.append(data.to_dict())

        with open(self.data_path, "w", encoding = "utf-8") as file:
            json.dump(temporary_list, file, indent = 4)
        
        return

    def show_leaderboard(self) -> None:
        """Displays the leaderboard."""
        
        data = self.load_data()

        data = sorted(data, key = lambda x: x.score, reverse=True)

        utils.print_section_header("Leaderboard")

        for index, player in enumerate(data, start = 1):
            print(f"{index}. {player.name} - {player.score}")
        
        utils.print_section_footer("End")

    def log_in(self) -> str:
        data = self.load_data()

        while True:
            username = utils.get_valid_input(str, "Username: ")
            username = username.strip().lower()

            # Optional: allow user to quit
            if username == "exit":
                return None  # or handle exit

            password = utils.get_valid_input(str, "Password: ")

            if any(player.name == username and player.password == password for player in data):
                print("Logged In Successfully!\n")
                return username
            else:
                print("Incorrect Credentials! Try again.\n")
                


    def sign_up(self) -> str:
        """Takes inputs for new user's credentials and saves it in the data file"""

        data = self.load_data()
        
        # Inputs...
        while True: 
            username = utils.get_valid_input(str, "Name: ")
            username = username.strip().lower()

            if any(player.name == username for player in data):
                print("Username is already taken!")
                print("Try Again!\n")
                continue

            break

        while True:
            password = utils.get_valid_input(str, "Password: ")
            confirm_password = utils.get_valid_input(str, "Confirm Password: ")

            if password == confirm_password:
                break

            print("Password and Confirm Password can't be different. Enter again!\n")
        
        new_player = Player(username, password, score = 0)
        data.append(new_player)
        self.save_data(data)
        utils.print_section_footer("New Player Added Successfully!")

        return username
    
    def score_updater(self, username: str ,score: int) -> None:
        
        data = self.load_data()

        for player in data:
            if username == player.name:
                player.score = player.score + score
                self.save_data(data)
                return
            
        print(f"Couldn't find {username} in data")
        
        