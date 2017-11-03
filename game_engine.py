from word_game import Word_game
from os import listdir


class Player:
    """
    A player which plays games
    """
    number_of_games = 0
    points = 0

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print('Hello {}!'.format(self.player_name))
        print('You are {}')

    def new_game(self, file_path):
        print('Starts a new game')
        self.number_of_games = self.number_of_games + 1
        self.game = Word_game(file_path)
        self.game.print_words()

    def make_a_guess(self, guess):
        """
        User makes a guess
        ARGS: guess - a string with the guess of the odd word_game
        RETURNS: True if guess was correct, otherwise 0
        """
        if(self.game.make_a_guess(guess)):
            self.points = self.points + 1
            self.print_progress()
            return(True)
        else:
            return(False)

    def print_progress(self):
        print('{} is playing game {} with a total score of {}'.format(
            self.name, self.number_of_games, self.points))

    def quit_game(self):
        print('GAME IS FINISHED!')
        print('-----------------------------')
        print('Player: {}'.format(self.name))
        print('Number of games: {}'.format(self.number_of_games))
        print('With a cumulative score of: {}'.format(self.points))


def choose_game():
    """
    Browses the games/ folder and let's the player pick a game
    """

    list_of_contents = [f for f in listdir('games/') if '.txt' in f]

    # Print possible games
    print('Choose between: ')
    for num, game in enumerate(list_of_contents):
        print('{}. {}'.format(num+1, game))

    # Check input
    try:
        choice = int(input('What game do you want to play?' +
            'You need to input an integer'))
    except ValueError:
        print('You need to input an integer')
    try:
        game_name = list_of_contents[choice-1]
    except IndexError:
        print('Your choice was not in the list')
    return(game_name)


def menu(player_name):
    player = Player(name=player_name)
    print('{}, what do you want to do?'.format(player_name))
    while True:
        print('\n 1. Start a new game \n 2. Print progress \n 3. Quit game')
        try:
            choice = int(input())
        except ValueError:
            print('You need to pick an integer')
        if choice == 1:
            player.new_game('games/' + choose_game())
            input('Make a guess')
            player.make_a_guess(guess=guess)
        # print progress
        if choice == 2:
            player.print_progress()
        # quit game
        if choice == 3:
            player.quit_game()
            break
        elif choice not in [1, 2, 3]:
            print('You need to choose something from the list')


def main():
    # Create a player
    player_name = input('What is your name?')
    player1 = Player(name=player_name)
    # Starting a new game
    menu(player_name)
if __name__ == '__main__':
    main()
