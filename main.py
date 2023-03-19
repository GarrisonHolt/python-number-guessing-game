from GameClass import *

name = input('Enter your name: ')

game = Game(name)


if __name__ == '__main__':
    game.start_game()
    game.game()