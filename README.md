# Introducing odd_one_out_game, a simple game build on non-simple methods

This is a silly game that illustrated a pretty silly use case for the Google pretrained Word2Vec embeddings. 

## One-Odd-Out Game

The concept of the game is simple: given 4 words, choose the word that doesn't belong in the group. For example, if given the words *King*, *Queen*, *Prince* and *Cleaner* we might guess that the odd one out is *Cleaner*.

There are a few prepared game files in the games/ folder. They can be created using the create_new_pairs.py file. Note that it requires a pretrained word2vec model such as [this one](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit).


## Usage

- game_enginge.py 

Is the file you need to run to play the game. In default the game can be run in the console. It creates an object of the player class and starts a new game by giving the file path to one of the files in the games/ folder.

- word_page.py
Contains the implementation of the game with the methods called from the game engine to make guesses etc.

- create_new_pairs.py
Used to create new game files by coming up with four words.
