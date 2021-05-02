numGuests = int(input())

guestRooms = {}

roomAssignments = [int(x) for x in input().split(' ')]

for room in roomAssignments:
    if room not in guestRooms:
        guestRooms[room] = 1
    elif room in guestRooms:
        guestRooms[room] += 1

for key, value in guestRooms.items():
    if value == 1:
        print(key)
