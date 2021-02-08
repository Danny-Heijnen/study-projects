# Import OS for clearing the screen in the function encounter(). This is not currently in use, but can be uncommented when using the program in a Linux or Windows terminal.
#import os


# Describe a class Player that can be used in the different encounters.
class Player:

    # Initiate a Player class to create a player with 2 health and 0 health potions. This player will be used to play the game.
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
def encounter(player, room_text, attack_text, flee_text, potion_text):

    # Command to clear the terminal screen in Windows and Linux. (Doesn't work in PyCharm, but preferred in a Windows or Linux terminal)
    #os.system("cls" if os.name == "nt" else "clear")

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
    print("\n" + room_text + "\n")

    # Describe the choice to attack or flee.
    print("You can choose to attack the creature (1), or to flee (2)")

    # If the player has at least 1 potion, give the option to take a potion.
    if player.has_potion():
        print("You can also use a potion (3) to increase your health by 1 point.")

    # Request an action from the player.
    action = input("\nWhat action do you want to take? ")

    # Print the appropriate text for the chosen action.
    if action == "1":
        print("\n" + attack_text)
    elif action == "2":
        print("\n" + flee_text)
    elif action == "3":
        print("\n" + potion_text)
        player.use_potion() # If the player uses a potion: Increase health, decrease number of potions.


# Pause for a moment and allow the player to choose when to proceed to the next room.
def next_encounter():

    # Request an <enter> to proceed.
    input("\nPress <enter> to advance to the next room:")


def main():

    # Create a player
    player1 = Player()



    # Start the first encounter.
    encounter(player1, "You enter a hall with a goblin.\nHe looks angry that you disturbed his feast of flame-grilled adventurer.\nHe stands up, dagger in hand and begins to approach you.",
              "You attack the goblin, his menacing voice lets out a last squeal as he is cleft in twin by your longsword.",
              "You quickly dart past the goblin with a nimble zig-zag.\nYou manage to sneak throught the door at the other end of the hall as you firmly close it behind you with a loud bang.",
              "You take a health potion, increasing you health by 1 point.\nYou manage to hold the goblin at bay with you shield and shove him out of the way.\nThen you leave the room, using the door at the far end of the hall.")
    next_encounter()

    # Give the player a potion.
    player1.add_potion()

    # Start the next encounter to see if the added potion changes the dialogue.
    encounter(player1,
              "You enter a hall with a goblin.\nHe looks angry that you disturbed his feast of flame-grilled adventurer.\nHe stands up, dagger in hand and begins to approach you.",
              "You attack the goblin, his menacing voice lets out a last squeal as he is cleft in twin by your longsword.",
              "You quickly dart past the goblin with a nimble zig-zag.\nYou manage to sneak throught the door at the other end of the hall as you firmly close it behind you with a loud bang.",
              "You take a health potion, increasing you health by 1 point.\nYou manage to hold the goblin at bay with you shield and shove him out of the way.\nThen you leave the room, using the door at the far end of the hall.")
    next_encounter()

main()

