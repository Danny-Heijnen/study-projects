import os

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


room_object_list = []

for file_name in os.scandir("./Rooms"):

    file = open(file_name)

    list_of_lines = []

    for line in file:
        list_of_lines.append(line[:-1])

    room_object_list.append(Room(*list_of_lines))

for room in room_object_list:
    print(room.get_text_room_name())
    print(room.get_text_attack())
