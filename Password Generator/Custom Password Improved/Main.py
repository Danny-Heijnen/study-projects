import secrets
import sys


# Return the strength of the password.
def return_strength(number_of_chars, lower, upper, number, special_char):

    list_of_choices = [lower, upper, number, special_char]

    if number_of_chars >= 16:
        return "strong"
    elif number_of_chars > 12 and list_of_choices.count("y") >= 3:
        return "strong"
    elif number_of_chars >= 8 and list_of_choices.count("y") == 4:
        return "strong"
    else:
        return "weak"


# Request numerical input from the user.
def get_numerical_input(prompt):
    value = input(prompt)
    while not value.isnumeric():
        value = input("You have not entered a number, please enter a number: ")
    return int(value)


# Request a yes or no input from the user.
def get_yes_or_no_input(prompt):
    value = input(prompt).lower()
    while value != "y" and value != "n":
        value = input("You have to answer (y)es or (n)o: ").lower()

    return value


def main():

    # Print introduction.
    print("This is a custom password generator.\n")

    # Request input from the user to generate the password.
    number_of_characters = get_numerical_input("Please enter the desired number of characters for the password: ")
    lower_case_choice = get_yes_or_no_input("Do you want lower case letters in the password? (y/n) ")
    upper_case_choice = get_yes_or_no_input("Do you want upper case letters in the password? (y/n) ")
    numbers_choice = get_yes_or_no_input("Do you want numbers in the password? (y/n) ")
    special_characters_choice = get_yes_or_no_input("Do you want special characters in the password? (y/n) ")

    # Create an empty string that will hold the choices for the characters:
    possible_character_string = ""

    # Add a category of characters to the , depending on the choices of the user.
    if lower_case_choice == "y":
        possible_character_string += "abcdefghijklmnopqrstuvwxyz"

    if upper_case_choice == "y":
        possible_character_string += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if numbers_choice == "y":
        possible_character_string += "0123456789"

    if special_characters_choice == "y":
        possible_character_string += "!@#$%^&*()_+-=[]{};:,<.>/?"

    if lower_case_choice == "n" and upper_case_choice == "n" and numbers_choice == "n" and special_characters_choice == "n":
        print("\nIt is impossible to create a password without characters. The program will exit.")
        sys.exit()

    if number_of_characters <= 0:
        print("\nIt is impossible to create a password without characters. The program will exit.")
        sys.exit()

    # Create an empty string that will contain the password.
    password = ""

    # Create a password for the user by adding a random character of the chosen kinds to the password.
    for i in range(number_of_characters):
        password += secrets.choice(possible_character_string)

    # Print the password to the user.
    print("\nYour password is: " + password)

    # Print the strength of the password.
    print("The strength of your password is: " + return_strength(number_of_characters, lower_case_choice, upper_case_choice, numbers_choice, special_characters_choice))


main()
