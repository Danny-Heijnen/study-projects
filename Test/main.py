number_of_rooms = input("How many rooms do you want to play? ")

while number_of_rooms > 4:
    number_of_rooms = input("There are only 4 rooms. How many rooms do you want to play? ")

for i in range(number_of_rooms):
    random_room =