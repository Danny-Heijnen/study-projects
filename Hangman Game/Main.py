# This is a small 2 player hangman game. Player 1 enters a word to guess and player 2 gets a number of guesses.

# import os to use for clearscreen.
import os


# A player class that has a name and a score.
class Player:
    def __init__(self):
        self.score = 0

    def set_player_name(self, player_name):
        self.name = player_name

    def get_player_name(self):
        return self.name

    def give_points(self, points):
        self.score += points

    def get_points(self):
        return self.score


# Request a player name.
def get_name(prompt):

    value = input(prompt)
    while not value.isalpha() or not 0 < len(value) < 40:
        value = input('Please enter your name with only letters: ')
    return value


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


# Request a user input for the amount of rounds.
def get_number(prompt):
    value = input(prompt)
    while not value.isnumeric() or int(value) <= 0:
        value = input("You have not entered a valid number, please enter a number higher than 0: ")
    return int(value)


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


# Play 1 round of hangman.
def play_round(player_a, player_b):
    # Clear the terminal screen.
    clear_screen()

    # Request a target word from Player 1.
    target_word = get_word(player_b.get_player_name() +
                           ', please turn away from the screen.\n\n' + player_a.get_player_name() + ', please enter a word that ' + player_b.get_player_name() + ' needs to guess: ')
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
        print(player_b.get_player_name() + ', it is your turn to guess the word.\n')

        # Show the guessed_string.
        print('Target word: ' + guessed_string)

        # Show the guessed letters.
        print('Letters you have used so far: ' + guessed_letters)

        # Show the number of guesses remaining.
        print('Wrong guesses remaining: ' + str(8 - failed_guesses) + '\n')

        # Request a letter from Player 2.
        letter = get_letter('Please enter a letter to guess: ')

        # Make sure the letter is not tried before, if it is, request a new letter.
        while letter in guessed_letters:
            letter = get_letter(
                'You have already tried this letter. Please enter a new letter: ')

        # Add the chosen letter to the list of guessed letters
        guessed_letters += letter

        # Update the guessed_string.
        guessed_string = update_guessed_string(target_word, guessed_string, letter)

        # Update the number of failed guesses.
        if letter not in target_word:
            failed_guesses += 1

    # Update the scores, tell the players who has won the game and what the answer was.
    if check_for_win(target_word, guessed_string):
        player_b.give_points(1)
        print('\nThe word is: ' + guessed_string +
              '! ' + player_b.get_player_name() + ' wins this round! You have guessed the word!')
    else:
        player_a.give_points(1)
        print('\nThe word is: ' + target_word + '! ' +
              player_a.get_player_name() + ' wins this round! ' + player_b.get_player_name() + ' has guessed too many times.')

    # Show the current score.
    print('\nThe current score is:')
    print(player1.get_player_name() + ': ' + str(player1.get_points()) + ' points')
    print(player2.get_player_name() + ': ' + str(player2.get_points()) + ' points')

    global number_of_rounds_left
    number_of_rounds_left -= 1

    # Show how many rounds are left.
    print('\nThere are ' + str(number_of_rounds_left) + ' rounds left to play.')

    # Wait for player input to advance to the next round or the score screen.
    if number_of_rounds_left > 0:
        input('\nPress <enter> to continue to the next round.')
    else:
        input('\nThe game is finished. Press <enter> to continue to the score screen.')


def main():

    # Clear the terminal screen.
    clear_screen()

    # Print an intruduction about the game.
    print('Welcome to this game of hangman!\n\nThe rules of the game are as follows:\n')

    # Print the rules of the game.
    print('Player 1 will choose a word between 1 and 35 characters long.\nPlayer 2 then has to guess the word by choosing letters. Player 2 chooses the letters one by one.\nIf a letter is correct, the game will show where the letter occurs in the word.\nIf a letter is wrong, Player 2 gets a new chance to choose a letter.\nAfter 8 wrong choices the game ends.\n\nPlayer 1 wins if Player 2 has made 8 wrong guesses.\nPlayer 2 wins if the word is guessed correctly with 7 or less wrong guesses.\nThe winner of a round gets 1 point. A full set consists of 2 rounds, so there are 2 points to a set.\nAfter each round, the other player may choose a word.\n')

    # Ask for a keystroke to continue and wish the players good luck.
    input('Good luck and have fun!\n\nPress <enter> to continue.')

    # Clear the terminal screen.
    clear_screen()

    # Declare 2 global player variables.
    global player1, player2

    # Create a player object for each player.
    player1 = Player()
    player2 = Player()

    # Ask the players to fill in their names.
    player1.set_player_name(get_name('Player 1, please enter your name: '))
    player2.set_player_name(get_name('Player 2, please enter your name: '))

    # Ask the players how many sets to play.
    print('\nA full sets consists of each 2 rounds. After every round the other player chooses a word.\n')
    number_of_sets = get_number('How many sets do you want to play? ')

    # Declare a global variable for the number of rounds remaining.
    global number_of_rounds_left

    # Initialize the number of rounds left.
    number_of_rounds_left = number_of_sets * 2

    # Play a full set where a different player starts every round.
    for i in range(number_of_sets):

        play_round(player1, player2)
        play_round(player2, player1)

    # Clear the terminal screen.
    clear_screen()

    # Show who has won the game.
    if player1.get_points() > player2.get_points():
        print(player1.get_player_name() + ' has won the game with ' + str(player1.get_points()) +
              ' points against ' + str(player2.get_points()) + '. Well done!')
    elif player2.get_points() > player1.get_points():
        print(player1.get_player_name() + ' has won the game with ' + str(player2.get_points()) +
              ' points against ' + str(player1.get_points()) + '. Well done!')
    elif player1.get_points() == player2.get_points():
        print('This game is a tie between ' + player1.get_player_name() +
              ' and ' + player2.get_player_name() + ' with ' + str(player1.get_points()) + ' points each. Well done to both of you!')

    # Wait for a keystroke in order to end the game.
    input('\nPress <enter> to exit the game.')

    # Clear the terminal screen.
    clear_screen()


main()
