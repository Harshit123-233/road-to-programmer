from hangman_game import HangMan
from player_manager import PlayerManager
import utils


def first_screen():
    """first screen a user will see when the program is executed"""

    print("""
1. Sign Up
2. Log In
3. Guest (Progress won't be saved!)
\n""")

    while True:

        user_choice = utils.get_valid_input(int, "Enter: ")

        if user_choice == 1:
            return utils.PlayerAuthType.SIGNUP
        elif user_choice == 2:
            return utils.PlayerAuthType.LOGIN
        elif user_choice == 3:
            return utils.PlayerAuthType.GUEST
        else:
            print("Invalid Input! Please enter an integer (1-3).\n")

def auth_screen(auth_type: utils.PlayerAuthType):

    auth = PlayerManager()

    if auth_type == utils.PlayerAuthType.SIGNUP: 
        username = auth.sign_up()
        return username

    elif auth_type == utils.PlayerAuthType.LOGIN:
        username = auth.log_in()
        return username
    
    else:
        return utils.PlayerAuthType.GUEST
    
def main(username: str) -> None:

    hangman = HangMan()
    manager = PlayerManager()
    utils.print_section_header("Welcome To Hangman")

    if username == utils.PlayerAuthType.GUEST:
        print("You can play only once and that also in easy mode!")
        score = hangman.game_round(utils.RoundType.EASY)
        print(f"You scored {score}. You can log in or sign up to play more and access other features like view leaderboards!")
        print("Anyways, thanks for playing Hangman!\n")
        exit()

    while True:
        utils.show_features()
        user_choice = utils.get_valid_input(int, "Enter: ")

        if user_choice == 1:
            utils.show_difficulty()

            user_difficulty_choice = utils.get_valid_input(int, "Enter: ")

            if user_difficulty_choice in (1,2,3,4):

                if user_difficulty_choice == 1:
                    score = hangman.game_round(utils.RoundType.EASY)
                    manager.score_updater(username, score)
                elif user_difficulty_choice == 2:
                    score = hangman.game_round(utils.RoundType.MEDIUM)
                    manager.score_updater(username, score)
                elif user_difficulty_choice == 3: 
                    score = hangman.game_round(utils.RoundType.HARD)
                    manager.score_updater(username, score)
                else: 
                    score = hangman.game_round(utils.RoundType.BONUS)
                    manager.score_updater(username, score)
            else:
                print("Enter a valid number!")
                continue

        elif user_choice == 2:
            manager.show_leaderboard()
            proceed = input("Press enter to continue!")
            continue

        elif user_choice == 3:
            utils.show_rules()
            proceed = input("Press enter to continue!")
            continue

        elif user_choice == 4:
            utils.print_section_footer("Thanks for playing Hangman!")
            break

        else:
            print("Invalid Input! Please enter a valid option!")

if __name__ == "__main__":

    auth_type = first_screen()

    main(auth_screen(auth_type))