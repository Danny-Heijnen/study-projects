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

    # Add 1 potion to the inventory of the player.
    def add_potion(self):
        self.potion += 1

def main():

    # Here are several tests to see if the object Player functions as planned.
    player1 = Player()

    print(player1.health)
    print(player1.potion)

    player1.add_potion()
    print(player1.health)
    print(player1.potion)

    print(player1.has_potion())

    player1.use_potion()
    print(player1.health)
    print(player1.potion)

    player1.has_potion()

    player1.deal_damage(1)
    print(player1.health)
    print(player1.potion)

    print(player1.is_player_alive())
    player1.deal_damage(2)

    print(player1.is_player_alive())
    print(player1.get_player_health())

    player1.use_potion()
    print(player1.health)
    print(player1.potion)

    player1.add_potion()
    player1.add_potion()

    print(player1.health)
    print(player1.potion)

    player1.use_potion()
    player1.use_potion()

    print(player1.health)
    print(player1.potion)

    print(player1.is_player_alive())

main()