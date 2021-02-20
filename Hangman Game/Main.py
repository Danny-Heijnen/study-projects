# This is a small 2 player hangman game. Player 1 enters a word to guess and player 2 gets a number of guesses.

def get_word(prompt):

    value = input(prompt).lower()


def main():

    word = get_word('Please enter a word that player 2 needs to guess: ')
