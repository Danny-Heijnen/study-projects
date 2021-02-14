import secrets


# TODO define function to return the strength of the password
def return_strength(number_of_chars, capital, number, special_char):
    pass


# Choose a lower case letter.
def choose_lower_case():
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    return secrets.choice(lower_case)


# Choose an upper case letter.
def choose_upper_case():
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return secrets.choice(upper_case)


# Choose a number.
def choose_number():
    numbers = '0123456789'
    return secrets.choice(numbers)


# Choose a special character.
def choose_special_character():
    special_characters = '!@#$%^&*()-_=+,.<>/?'
    return secrets.choice(special_characters)


# Request numerical input from the user.
def get_numerical_input(prompt):
    value = input(prompt)
    while not value.isnumeric():
        value = input("You have not entered a number, please enter a number: ")
    return int(value)


def main():

    # Test
    print(choose_lower_case())
    print(choose_upper_case())
    print(choose_number())
    print(choose_special_character())

# TODO how do you want to choose the characters? It needs to be as random as possible as well.


main()
