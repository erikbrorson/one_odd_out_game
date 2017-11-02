
from word_game import word_game

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
        self.game = word_game(file_path)
        self.game.print_words()

    def make_a_guess(self, guess):
        if(self.game.make_a_guess(guess)):
            self.points = self.points + 1
            self.print_progress()

    def print_progress(self):
        print('{} is playing game {} with a total score of {}'.format(
            self.name, self.number_of_games, self.points))        

    def quit_game(self):
        print('GAME IS FINISHED!')
        print('-----------------------------')
        print('Player: {}'.format(self.name))
        print('Number of games: {}'.format(self.number_of_games))
        print('With a cumulative score of: {}'.format(self.points))


def main():
    # Create a player
    player_name = input('What is your name?')
    player1 = Player(name=player_name)
    
    # Starting a new game
    player1.new_game('games/Am-I-Is-The.txt')
    
    # Make a guess
    guess = input('Make a guess')
    player1.make_a_guess(guess)

    # Quit game
    player1.quit_game()
if __name__=='__main__':
    main()



