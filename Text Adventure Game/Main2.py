# Text Adventure Game main.py
# This program is a short game that lets the player play a few rooms in a text adventure.


# Import OS for the scandir() function.
import os

# Import random for the randrange() function.
import random


# A class Room that will be used in the encounters.
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


# A class Player that can be used in the different encounters.
class Player:

    # Initialize a Player object to create a player with 2 health and 0 elixirs.
    # This player will be used to play the game.
    def __init__(self):
        self.health = 2
        self.elixir = 0

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

    # Decrease the number of elixirs by 1, and increase the health of the player by 1.
    def use_elixir(self):
        if self.elixir > 0:
            self.health += 1
            self.elixir -= 1

    # Check if the player has the elixir. Return True if the player has 1 or more elixirs. Return False if the player has none.
    def has_elixir(self):
        if self.elixir > 0:
            return True
        if self.elixir <= 0:
            return False

    # Add 1 elixir to the inventory of the player.
    def add_elixir(self):
        self.elixir += 1


# Let the player find the elixir.
def find_elixir(player):

    # Give an elixir to the player.
    player.add_elixir()

    # Print a message that indicates that an elixir has been found.
    print("\nIn this room you find the famous elixir that you have been looking for.\nThe red liquid is so bright, it seems to glow.\nYou notice small glimmers of light or reflecions, it is hard to tell, but the sight is mesmerizing.\nYou carefully place the elixir in your bag.\n")


# Let the player use an elixir.
def use_elixir(player):

    # Remove an elixir from the player.
    player.use_elixir()

    # Print a message to indicate that an elixir has been used and the effect on the hit points of the player.
    print("\nYou pull out the health potion and look at it.\nYou realize that this is the reason you came to this dungeon in the first place.\nBut you also know that you need it to survive.\n\nYou drink the life-giving red fluid and feel your life force return.")

    print("\nYour remaining hit points are now: " + str(player.get_player_health()))


# Perform an attack action.
def attack_action(player, room):

    # Determine the chance of a succesful attack. Current ration is 2/4, or 50%.
    chance = random.randrange(4)

    # Depending on the outcome, determine if the attack was succesful. If not, reduce the hit points by 1.
    if chance < 2:
        print("\n" + room.get_text_attack_success())
    else:
        player.deal_damage()
        print("\n" + room.get_text_attack_fail())


# Perform a flee action.
def flee_action(player, room):

    # Determine the chance of a succesful flight. Current ratio is 3/4, or 75%.
    chance = random.randrange(4)

    # Depending on the outcome, determine if the flight was succesful. If not, reduce the hit points by 1.
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
def play_encounter(player, room, room_index, final_room_index):

    # Clear the terminal screen.
    os.system('cls' if os.name == 'nt' else 'clear')

    # Tell the user how many hit points are remaining.
    print("Hit points remaining: " + str(player.get_player_health()))

    # Give the player a health potion at the start of room 2.
    if room_index == 1:
        find_elixir(player)

    # Let the player know whether (s)he has an elixir.
    if player.has_elixir():
        print("You have the elixir in your posession.")
    else:
        print("You don't have the elixir.")

    # Print the description of the current room or situation.
    print("\n" + room.get_text_description() + "\n")

    # Describe the choice to attack or flee.
    print("You can perform the following actions:\n(1) Attack the creature\n(2) Flee from the creature")

    # If the player has at least 1 potion, give the option to take a potion.
    if player.has_elixir():
        print("(3) Use the elixir")

    # Set a sentinel value for action.
    action = "a"

    # Request an action from the player.
    if player.has_elixir():
        while not input_validation2(action):
            action = input("\nWhat action do you want to take? ")

    if not player.has_elixir():
        while not input_validation3(action):
            action = input("\nWhat action do you want to take? ")

    action = int(action)

    # If the player chooses to drink an elixir, perform that action and request the next action.
    if action == 3:
        use_elixir(player)

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
    if player.is_player_alive() and player.has_elixir():
        print("\nVictory! You escaped the dungeon with your life and the elixir!")
        input("\nPress <enter> to exit the program and continue your adventures.")
    # Indicate a loss.
    elif not player.is_player_alive():
        print("\nYou died. The game is over.")
        input("\nPress <enter> to exit the program.")
    # Indicate a draw.
    elif player.is_player_alive() and not player.has_elixir():
        print("\nYou have escaped the dungeon with your life. But you don't have the elixir.")
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

    # Print the introduction of the game to the player.
    print("Welcome, adventurer, to the dungeon of hope and despair.\nNot just despair? Oh no dear traveler, hope and despair.\nFor in this dungeon can be found the elixer of(a little bit more) life.\nOne sip of this miraculous health-restoring potion can moderately increase your health.\nUnfortunately the small flask only holds one sip...\nAnd the dungeon houses many dangerous creatures.\n\nWill you be able to find the elixer and escape the dungeon with your life?\nOr perhaps you will need the elixer just to survive the horrors that await you, \nleaving you as empty-handed as when you started, but at least with a beathing heart in your body.\nOnly time will tell...\n\nVenture forth, adventurer, and let's see how your story unfolds.\n")

    # Allow the player to start the game when (s)he is ready.
    input("Press <enter> to start the game.\n")

    # Create a room_playlist.
    room_playlist = create_room_playlist()

    # Play an encounter for every room in the playlist.
    for i in range(len(room_playlist)):

        # Play the next encounter.
        play_encounter(player1, room_playlist[i], i, len(room_playlist))

        # Stop playing if the player's health reaches 0 after a round.
        if player1.get_player_health() <= 0:
            break

        # Ask to proceed to the next room if the game is not finished.
        if i < len(room_playlist) - 1:
            # Request an <enter> to proceed to the next room.
            input("\nPress <enter> to advance to the next room.")

    # Check if the game is a win, loss or draw for the player.
    win_loss_draw(player1)


main()
