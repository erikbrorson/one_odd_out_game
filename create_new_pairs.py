import numpy as np
import gensim
from scipy import spatial

"""
Creates new games using word embeddings imported from the Google Word2Vec model
"""

def cosine_dist(first_word, second_word):
    """
    Computes the cosine distance between two vectors
    """
    return(spatial.distance.cosine(first_word, second_word))

class game_generator:

    word_dict = {}
    odd_one_out = ''
    sum_of_distance = {}
    
    def __init__(self, words, file_url_to_w2v_model='/Volumes/PICS/pyProject/GoogleNews-vectors-negative300.bin.gz'):
        self.words = words
        self.words.sort()
        self.file_url_to_w2v_model = file_url_to_w2v_model

    def import_model(self):
        """
        Imports the Word2Vec model into memory
        """
        print('Importing Word2Vec embeddings')
        self.model = gensim.models.KeyedVectors.load_word2vec_format(self.file_url_to_w2v_model, binary=True)

    def extract_word_dict(self):
        """
        Computes 
        """

        print('Computing the word dictionary')
        for word in self.words:
            try:
                self.word_dict[word] = self.model.wv[word]
            except KeyError:
                print('{} does not exist in the model...'.format(word))

    def new_words(self, words):
        """
        Gets new words and resets values
        """
        self.words = words
        self.words.sort()

        # cleaning
        self.word_dict = {}
        self.odd_one_out = ''
        self.sum_of_distance = {}


    def print_words(self):
        print('The words are {}, {}, {}, and {}'.format(
            self.words[0], self.words[1], self.words[2], self.words[3]))

    def find_odd_out(self):
        """
        Find the odd word by returning the word with the highest sum of distances 
        """
        for word_one in self.word_dict.keys():
            ssd = 0
            word_two_list = list(self.word_dict.keys())
            word_two_list.remove(word_one)
            for word_two in word_two_list:
                ssd = ssd + cosine_dist(first_word=self.word_dict[word_one], 
                                        second_word=self.word_dict[word_two])
            self.sum_of_distance[word_one] = ssd
        self.odd_one_out = max(self.sum_of_distance, key=self.sum_of_distance.get)

    def write_to_file(self):
        """
        Writes games to file
        """
        file_name = '-'.join(self.words)

        file = open('games/'+file_name+'.txt', 'w')
        file.write(' '.join(self.words) + '\n')
        file.write(self.odd_one_out + '\n')
        for word, vector in self.word_dict.items():
            file.write(word + ' ' +','.join(str(vector)))
            file.write('\n')
        file.close()

def main():

    file_url_to_w2v_model = '/Volumes/PICS/pyProject/GoogleNews-vectors-negative300.bin.gz' # change this to local file path
    
    generator = game_generator(words=['King', 'Queen', 'Prince', 'Cleaner'])
    generator.import_model()
    generator.extract_word_dict()
    generator.find_odd_out()
    generator.write_to_file()

    generator.new_words(words=['Bicycle', 'Pump', 'Wheel', 'Cinnamon'])
    generator.print_words()
    generator.extract_word_dict()
    generator.find_odd_out()
    generator.write_to_file()

    generator.new_words(words=['Integral', 'Pythagoras', 'Addition', 'Christmas'])
    generator.print_words()
    generator.extract_word_dict()
    generator.find_odd_out()
    generator.write_to_file()

    generator.new_words(words=['Love', 'Friendship', 'Kindness', 'Hate'])
    generator.print_words()
    generator.extract_word_dict()
    generator.find_odd_out()
    generator.write_to_file()

    generator.new_words(words=['Three', 'Five', 'Seven', 'Thousand'])
    generator.print_words()
    generator.extract_word_dict()
    generator.find_odd_out()
    generator.write_to_file()

    generator.new_words(words=['The', 'Is', 'I', 'Am'])
    generator.print_words()
    generator.extract_word_dict()
    generator.find_odd_out()
    generator.write_to_file()

if __name__ == '__main__':
    main()