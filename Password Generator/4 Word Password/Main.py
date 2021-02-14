# Create a secure password by concatenating 4 random English words.

# Import secrets
import secrets


# Define a function to remove the last character of a string
def remove_newline(string):
    new_string = string[:-1]
    return new_string


# Define a function to securely select a given number of items from a given list.
def secure_select(list_of_words, number):
    secure_random = secrets.SystemRandom()
    list_of_random_items = secure_random.sample(list_of_words, number)
    return list_of_random_items


def main():

    # Create a list of words.
    word_list = []

    # Open the file that contains the words.
    file = open("WordlistMedium.txt")

    # Add every word in the file to the list of words, minus the newline character at the end.
    for line in file:
        word_list.append(remove_newline(line))

    # Use the secure_select function to choose 4 items from the total word list.
    password_list = secure_select(word_list, 4)

    # Create an empty string to add the password items to.
    password_string = ""

    # Add the password items to a string to create the password.
    for item in password_list:
        item_capitalized = item.capitalize()
        password_string = password_string + item_capitalized

    # Print the password for the user.
    print(password_string)


main()
