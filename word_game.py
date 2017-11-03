class Word_game:
    """
    An instance of the odd one out game
    """
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.words = file.readline().rstrip().split(' ')
            self.odd_one_out = file.readline().rstrip()

    def print_words(self):
        print('The words are: {}, {}, {}, and {}'.format(
            self.words[0], self.words[1], self.words[2], self.words[3]))

    def print_faulty_word(self):
        print('The odd word is {}'.format(self.odd_one_out))

    def make_a_guess(self, guess):
        if guess not in self.words:
            print('The guessed word is not in the list')
            return False
        if guess == self.odd_one_out:
            print('You were right!')
            self.exit()
            return(True)
        else:
            print('You guessed the wrong word!')
            return(False)

    def exit(self):
        print('You guessed the right word which was \"{}\", well done!'.format(self.odd_one_out))

