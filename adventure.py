# coding=utf-8
from data import locations

# Each direction is a set of coordinates which, when added to a position,
# # will move it in that direction.
# So for instance, if we’re currently at (1, 1), moving east
# will result in (1+1, 1) = (2, 1).
# Moving west will result in (1-1, 1) = (0,1).

directions = {
    "west": (-1, 0),
    "east": (1, 0),
    "north": (0, -1),
    "south": (0, 1)
}

position = (0, 0)

while True:
    location = locations[position]
    print "You are at the %s" % location

    valid_directions = {}

    for k, v in directions.iteritems():    # k, v -> key, value
        possible_position = (position[0] + v[0], position[1] + v[1])  # generates new position for each direction
        possible_location = locations.get(possible_position)  # .get is a dictionary method which returns None if that key doesn't exist
        if possible_location:
            print "To the %s is a %s" % (k, possible_location)
            valid_directions[k] = possible_position

    direction = raw_input("Which direction do you want to go?\n")
    position = valid_directions[direction]