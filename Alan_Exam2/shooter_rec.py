import random

# ROOM = random.randint(1, 500)
# Comment in the next line and choose 65 to test.
ROOM = 65
room_sizes = []
again = 'Y'
while again.upper() == 'Y':
    # print("Not found yet.")
    sqft = int(input("Enter square footage of room: \n"))
    room_sizes.append(sqft)
    again = input("Enter another room size? Y/N")
# maximum = max(room_sizes)

def found(list):
    next_room = list.pop()
    if next_room == ROOM:
        print(f"You found him in the {next_room} square foot room.")
    else:
        if len(list) > 0:
            return found(list)
        else:
            print("No shooter.")

found(room_sizes)
