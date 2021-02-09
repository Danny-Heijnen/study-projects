# Import OS for the scandir() function.
import os

# Import random for the randrange() function.
import random

# Describe a class Room that will be used in the encounters.
class Room:

    # Initialize a Room object to create a Room with 4 texts to use in the encounter.
    def __init__(self, room_name_text, description_text, attack_text, flee_text, health_potion_text):
        self.room_name = room_name_text
        self.description = description_text
        self.attack = attack_text
        self.flee = flee_text
        self.health_potion = health_potion_text

    def get_text_room_name(self):
        return self.room_name

    def get_text_description(self):
        return self.description

    def get_text_attack(self):
        return self.attack

    def get_text_flee(self):
        return self.flee

    def get_text_health_potion(self):
        return self.health_potion


# Describe a class Player that can be used in the different encounters.
class Player:

    # Initialize a Player object to create a player with 2 health and 0 health potions. This player will be used to play the game.
    def __init__(self):
        self.health = 2
        self.potion = 0

    # Return the current health of the player.
    def get_player_health(self):
        return self.health

    # Check if the player is still alive (has more than 0 hit points)
    def is_player_alive(self):
        if self.health > 0:
            return True
        if self.health <= 0:
            return False

    # Take an amount of damage away from the current hit points of the player.
    def deal_damage(self, damage):
        self.health = self.health - damage

    # Decrease the number of potions by 1, and increase the health of the player by 1.
    def use_potion(self):
        if self.potion > 0:
            self.health += 1
            self.potion -= 1

    # Check if the player has a potion. Return True if the player has 1 or more potions. Return False if the player has none.
    def has_potion(self):
        if self.potion > 0:
            return True
        if self.potion <= 0:
            return False

    def get_potions(self):
        return self.potion

    # Add 1 potion to the inventory of the player.
    def add_potion(self):
        self.potion += 1


# Render an encounter where the player enters a room and makes a choice.
def encounter(player, room):

    # Clear the screen. This is not an elegant solution, but os.system("cls") doesn't work because PyCharm works with a Python shell, not a real Windows terminal.
    print("\n" * 100)

    # Tell the user how many hit points are remaining.
    print("Hit points remaining: " + str(player.get_player_health()))

    # Check if the player has a potion. If True, print a line to tell the user how many potions are left. If False, do nothing.
    if player.has_potion():
        if player.get_potions() == 1:
            print("You have " + str(player.get_potions()) + " potion left.")
        else:
            print("You have " + str(player.get_potions()) + " potions left.")
    else:
        pass

    # Print the description of the current room or situation.
    print("\n" + room.get_text_description() + "\n")

    # Describe the choice to attack or flee.
    print("You can choose to attack the creature (1), or to flee (2)")

    # If the player has at least 1 potion, give the option to take a potion.
    if player.has_potion():
        print("You can also use a potion (3) to increase your health by 1 point.")

    # Request an action from the player.
    action = input("\nWhat action do you want to take? ")

    # Print the appropriate text for the chosen action.
    if action == "1":
        print("\n" + room.get_text_attack())
    elif action == "2":
        print("\n" + room.get_text_flee())
    elif action == "3":
        print("\n" + room.get_text_health_potion())
        player.use_potion() # If the player uses a potion: Increase health, decrease number of potions.


# Pause for a moment and allow the player to choose when to proceed to the next room.
def next_encounter():

    # Request an <enter> to proceed.
    input("\nPress <enter> to advance to the next room:")

# Add newline characters to the string after every dot to improve readability. Return the new string.
def add_newline(string):

    new_string = string.replace(". ", ".\n")

    return new_string


def main():

    # Create a player
    player1 = Player()

    # Create an empty list that will hold room objects.
    room_object_list = []

    # Create a room object for every text file in the directory ./Rooms and add them to the list room_object_list.
    for file_name in os.scandir("./Rooms"):

        # Open the text file
        file = open(file_name)

        # Create an empty list of lines to fill with the lines of text (strings).
        list_of_lines = []

        # Add the line to the list of lines. Take away the newline character at the end if there is one.
        for line in file:
            if line[-1] == "\n":
                list_of_lines.append(add_newline(line[:-1]))
            else:
                list_of_lines.append(add_newline(line))

        # Create a room object and add it to the list of room objects.
        room_object_list.append(Room(*list_of_lines))


    #TODO add a function or a few lines of code to create a a random selection of rooms from the list of room objects.

    number_of_rooms = input("How many rooms do you want to play? ")

        while number_of_rooms > 4:
            number_of_rooms = input("There are only 4 rooms. How many rooms do you want to play? ")

    for i in range(number_of_rooms):


    # Start the first encounter.
    encounter(player1, room_object_list[0])
    next_encounter()

    # Give the player a potion.
    player1.add_potion()

    # Start the next encounter.
    encounter(player1, room_object_list[1])


    next_encounter()

main()

