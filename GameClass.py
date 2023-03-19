import random 

class Game:
    def __init__(self, player_name) -> None:
        self.player_name = player_name

    def start_game(self):
        print(f'WELCOME TO THE GAME {self.player_name}')

    def game(self):
        player_choice = int(input('Enter a number between 1 - 10: '))
        computer_choice = random.randint(1,10)

        # While loop that controls the input
        while player_choice < 1 or player_choice > 10:
            print('Invalid choice....')
            player_choice = int(input('Enter a number between 1 - 10: '))
        else:
            pass


        # While loop that controls the game
        while player_choice != computer_choice:
            print('You Lose... Try again')
            print(f'The number was {computer_choice}')
            player_choice = int(input('Enter a number between 1 - 10: '))
            computer_choice = random.randint(1,10)
        else:
            print('Congratulations! You win!!')

