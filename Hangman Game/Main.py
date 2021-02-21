# This is a small 2 player hangman game. Player 1 enters a word to guess and player 2 gets a number of guesses.

# import os to use for clearscreen.
import os


# Request a user input of 1 word between 1 and 35 charcters that contains only letters.
def get_word(prompt):

    value = input(prompt).lower()
    while not value.isalpha() or not 0 < len(value) < 35:
        value = input(
            'Please enter a word with only letters that is between 1 and 35 characters: ').lower()
    return value


# Request a user input of 1 letter.
def get_letter(prompt):

    value = input(prompt).lower()
    while not value.isalpha() or not len(value) == 1:
        value = input('Please enter 1 letter: ').lower()

    return value


# Create a string with dots for each letter in the target word.
def create_guessed_string(target):

    guessed_string = ''

    for i in range(len(target)):
        guessed_string += '.'

    return guessed_string


# Check if the game is won.
def check_for_win(target, guess):
    if target == guess:
        return True
    else:
        return False


# Check if the game is lost.
def check_for_loss(guesses):
    if guesses >= 8:
        return True
    else:
        return False


# Create a new guessed string with the correctly guessed letters.
def update_guessed_string(target_string, guessed_string, letter):

    target_letter_list = list(target_string)
    guessed_letter_list = list(guessed_string)

    for i in range(len(target_letter_list)):
        if target_letter_list[i] == letter:
            guessed_letter_list[i] = letter

    return ''.join(guessed_letter_list)


# Clear the terminal screen.
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():

    # Clear the terminal screen.
    clear_screen()

    # Print an intruduction about the game.
    print('Welcome to this game of hangman!\n\nThe rules of the game are as follows:\n')

    # Print the rules of the game.
    print('Player 1 will choose a word between 1 and 35 characters long.\nPlayer 2 then has to guess the word by choosing letters.Player 2 chooses the letters one by one.\nIf a letter is correct, the game will show where the letter occurs in the word.\nIf a letter is wrong, Player 2 gets a new chance to choose a letter.\nAfter 8 wrong choices the game ends.\n\nPlayer 1 wins if Player 2 has made 8 wrong guesses.\nPlayer 2 wins if the word is guessed correctly with 7 or less wrong guesses.')

    # Ask for a keystroke to continue and wish the players good luck.
    input('Good luck and have fun!\n\nPress <enter> to continue.')

    # Clear the terminal screen.
    clear_screen()

    # Request a target word from Player 1.
    target_word = get_word(
        'Player 2, please turn away from the screen.\n\nPlayer 1, please enter a word that player 2 needs to guess: ')
    create_guessed_string(target_word)

    # Create a guessed_string that has dots for each letter in the target word. This string will be updated to contain the guessed letters.
    guessed_string = create_guessed_string(target_word)

    # Initialize a string that will contain the guessed letters.
    guessed_letters = ''

    # Initialize the counter with failed guesses.
    failed_guesses = 0

    # Play the game (ask for letters) as long as the game is not won or lost by Player 2.
    while not check_for_win(target_word, guessed_string) and not check_for_loss(failed_guesses):

        # Clear the terminal screen.
        clear_screen()

        # Show the Player who's turn it is.
        print('Player 2\n')

        # Show the guessed_string.
        print('Target word: ' + guessed_string)

        # Show the guessed letters.
        print('Letters you have used so far: ' + guessed_letters)

        # Show the number of guesses remaining.
        print('Wrong guesses remaining: ' + str(8 - failed_guesses) + '\n')

        # Request a letter from Player 2.
        letter = get_letter('Please enter a letter to guess: ')

        # Add the chosen letter to the list of guessed letters
        guessed_letters += letter

        # Update the guessed_string.
        guessed_string = update_guessed_string(target_word, guessed_string, letter)

        # Update the number of failed guesses.
        if letter not in target_word:
            failed_guesses += 1

    # Tell the players who has won the game and what the answer was.
    if check_for_win(target_word, guessed_string):
        print('\nThe word is: ' + guessed_string +
              '! Player 2 wins! You have guessed the word, congratulations!')
    else:
        print('\nThe word is: ' + target_word + '! Player 1 wins! You have guessed too many times.')


main()
