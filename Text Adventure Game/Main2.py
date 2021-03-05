# Text Adventure Game main.py
# This program is a short game that lets the player play a few rooms in a text adventure.


# Import OS for the scandir() function.
import os

# Import random for the randrange() function.
import random


# Describe a class Room that will be used in the encounters.
class Room:

    # Initialize a Room object to create a Room with 4 texts to use in the encounter.
    def __init__(self, room_name_text, description_text, attack_success_text, attack_fail_text, flee_success_text, flee_fail_text):
        self.room_name = room_name_text
        self.description = description_text
        self.attack_success = attack_success_text
        self.attack_fail = attack_fail_text
        self.flee_success = flee_success_text
        self.flee_fail = flee_fail_text

    def get_text_room_name(self):
        return self.room_name

    def get_text_description(self):
        return self.description

    def get_text_attack_success(self):
        return self.attack_success

    def get_text_attack_fail(self):
        return self.attack_fail

    def get_text_flee_success(self):
        return self.flee_success

    def get_text_flee_fail(self):
        return self.flee_fail


# Describe a class Player that can be used in the different encounters.
class Player:

    # TODO: set self.potion back to 0 for the real game.
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
    def deal_damage(self):
        self.health -= 1

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

    # Return the number of potions that the player has.
    def get_potions(self):
        return self.potion

    # Add 1 potion to the inventory of the player.
    def add_potion(self):
        self.potion += 1


# TODO:
def find_potion(player):

    player.add_potion()

    print("In the room you also find the famous health potion that you have been looking for.\nThe red liquid is so bright, it seems to glow.\nYou notice small glimmers of light or reflecions, it is hard to tell, but the sight is mesmerizing.\nYou carefully place the health potion in your bag.\n")


# TODO:
def use_potion(player):

    player.use_potion()

    print("\nYou pull out the health potion and look at it.\nYou realize that this is the reason you came to this dungeon in the first place.\nBut you also know that you need it to survive.\n\nYou drink the life-giving red fluid and feel your life force return.")

    print("\nYour remaining hit points are now: " + str(player.get_player_health()))


def attack_action(player, room):

    chance = random.randrange(4)

    if chance < 2:
        print("\n" + room.get_text_attack_success())
    else:
        player.deal_damage()
        print("\n" + room.get_text_attack_fail())


def flee_action(player, room):

    chance = random.randrange(4)

    if chance < 3:
        print("\n" + room.get_text_attack_success())
    else:
        player.deal_damage()
        print("\n" + room.get_text_attack_fail())


# Create a room_playlist with a number of room objects.
def create_room_playlist():

    # Create an empty list that will hold room objects.
    room_object_list = []

    # Create an empty list that will hold the current playlist of rooms.
    room_playlist = []

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

    # Set sentinel value:
    number_of_rooms = "a"

    # Ask the player how many rooms to play and randomly add that many rooms to the playlist.
    while not input_validation1(number_of_rooms):
        number_of_rooms = input(
            "Please enter a number between 0 and 4 for the number of rooms you want to play: ")

    # Convert the string input to an integer.
    number_of_rooms = int(number_of_rooms)

    # Pick a room at random from the the list with room objects. Add as many rooms as the player requested.
    while int(number_of_rooms) > 0:
        random_index = random.randrange(len(room_object_list))
        room_playlist.append(room_object_list[random_index])
        del room_object_list[random_index]
        number_of_rooms -= 1

    return room_playlist


# Render an encounter where the player enters a room and makes a choice.
def encounter(player, room, room_index, final_room_index):

    # Clear the terminal screen.
    os.system('cls' if os.name == 'nt' else 'clear')

    # Tell the user how many hit points are remaining.
    print("Hit points remaining: " + str(player.get_player_health()))

    # TODO:
    if player.get_potions() == 1:
        print("You have " + str(player.get_potions()) + " potion left.")
    else:
        print("You have no more health potions.")

    # Print the description of the current room or situation.
    print("\n" + room.get_text_description() + "\n")

    # Give the player a health potion at the start of room 2.
    if room_index == 1:
        find_potion(player)

    # Describe the choice to attack or flee.
    print("You can perform the following actions:\n(1) Attack the creature\n(2) Flee from the creature")

    # If the player has at least 1 potion, give the option to take a potion.
    if player.has_potion():
        print("(3) Use the health potion")

    # Set a sentinel value for action.
    action = "a"

    # Request an action from the player.
    if player.has_potion():
        while not input_validation2(action):
            action = input("\nWhat action do you want to take? ")

    if not player.has_potion():
        while not input_validation3(action):
            action = input("\nWhat action do you want to take? ")

    action = int(action)

    # TODO:
    if action == 3:
        use_potion(player)

        # Set a sentinel value for action.
        action = "a"

        # Request an action from the player.
        while not input_validation3(action):
            action = input("\nNext, do you want to attack (1) or flee (2)? ")

        action = int(action)

    # Print the appropriate text for the chosen action and change health and potions if a potions is used.
    if action == 1:
        attack_action(player, room)
    elif action == 2:
        flee_action(player, room)


# Check for a win, loss or draw
def win_loss_draw(player):

    # Indicate that the player has won the game.
    if player.get_player_health() > 0 and player.has_potion():
        print("\nVictory! You escaped the dungeon with your life and the health potion.")
        input("\nPress <enter> to exit the program and continue your adventures.")
    # Indicate a loss.
    elif player.get_player_health() <= 0:
        print("\nYou died. The game is over.")
        input("\nPress <enter> to exit the program.")
    # Indicate a draw.
    elif player1.get_player_health() > 0 and not player.has_potion():
        print("\nYou have escaped the dungeon with your life. But you had to leave the health potion behind.")
        input("\nPress <enter> to exit the program and continue your adventures.")


# Add newline characters to the string after every dot to improve readability. Return the new string.
def add_newline(string):
    return string.replace(". ", ".\n")


# Check if a given string is a number between 0 and 4 (inclusive).
def input_validation1(string):
    try:
        int(string)
        if 0 <= int(string) <= 4:
            return True
        else:
            return False
    except ValueError:
        return False


# Check if a given string is a number between 1 and 3 (inclusive).
def input_validation2(string):
    try:
        int(string)
        if 1 <= int(string) <= 3:
            return True
        else:
            return False
    except ValueError:
        return False


# Check if a given string is a number between 1 and 2 (inclusive).
def input_validation3(string):
    try:
        int(string)
        if 1 <= int(string) <= 2:
            return True
        else:
            return False
    except ValueError:
        return False


def main():

    # Clear the terminal screen.
    os.system('cls' if os.name == 'nt' else 'clear')

    # Create a player
    player1 = Player()

    # Create a room_playlist.
    room_playlist = create_room_playlist()

    # Play an encounter for every room in the playlist.
    for i in range(len(room_playlist)):

        # Play the next encounter.
        encounter(player1, room_playlist[i], i, len(room_playlist))

        # Stop playing if the player's health reaches 0 after a round.
        if player1.get_player_health() <= 0:
            break

        # Ask to proceed to the next room if the game is not finished.
        if i < len(room_playlist) - 1:
            # Request an <enter> to proceed to the next room.
            input("\nPress <enter> to advance to the next room:")

    # Check if the player has won, lost or drew the game.
    win_loss_draw(player1)


main()