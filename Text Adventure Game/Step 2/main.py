from random import randrange

print("You wake up early in the morning in a forest, next to a burnt-out bonfire.\nA stone's throw away you can see a road.\n")
direction = input("Do you want to go north (1) or south (2) on that road? ")

if direction == "1":
    print("You have gone north. After a few miles you find a stone with a strange green glow. You pick up the stone and put it in your pocket.")
else:
    print("You have gone south. Past a bend in the road, you find an abandoned hut. You decide to make the hut your home and explore the area around it.")

print("All of a sudden, you see a small band of 5 goblins approaching in the distance, they don't seem to have spotted you so far.\n")
attack = input("Do you want to attack (1) or go off the path to hide (2)? ")

if attack == "1":
    outcome_fight = randrange(3)

    print("You step off the path, draw your sword and wait until the goblins are closer."
          "When you hear their squealing voices loud and clear, you charge onto the path and attack the goblins")

    if outcome_fight < 1:
        print("You fight your way through the goblin band. You find a small hand crossbow and 2 bolts on one of the goblins.")
    else:
        print("The band of goblins overwhelms you and they take you captive. You are taken to the goblin leader to decide your fate.")
else:
    outcome_hiding = randrange(3)

    print("You step of the path and carefully walk deep into the forest.")

    if outcome_hiding < 2:
        print("The goblins haven't noticed a thing, you hear them pass as they talk loudly amongst themselves.")
    else:
        print("Apparently your scent has lingered on the path, you should have taken a bath. You see one of the goblins sniff around and advancing towards you. The rest of the goblins follow excitedly. It's no use to run and you aren't prepared to fight. You let yourself be taken captive and are taken to the leader of the goblins")
