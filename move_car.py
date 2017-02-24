# Refactored from kcamrine at Insight
# Callie Bradley, callie.m.bradley@gmail.com
# February 2017
# Run with Python 2.7, compiled with PyCharm

# This code takes input to describe vehicle location and movement.
# It outputs the new location

# Still to add:
## Unit tests, try/except better error handling
## User inputs should be grouped together in the code
## Typo in vehicle_two below
## Write code in methods, avoid global variables. Don't reference global variables inside the class
## dir could be a protected variable (for directory), should avoid

class Vehicle():
    """ Class to describe the vehicle coordinates """
    def __init__(self, x, y, face, maxx, maxy):
        self.x = x
        self.y = y
        self.face = face
        self.max_x = maxx
        self.max_y = maxy
        self.directions = ['N','E','S','W']
        self.movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}
        self.commands = {'L': 'turn_left', 'R': 'turn_right', 'M': 'move', 'B': 'back'}


class Movement():
    """ Class to describe vehicle movement """
    def input(self):
        print "Welcome to vehicle descriptorland!"
        print "You can input two vehicles' location and movement in the following way:"
        print "    xmax ymax"
        print "    x1 y1 face1"
        print "    movement1"
        print "    x2 y2 face2"
        print "    movement2"
        print ""
        print "Where:"
        print "    - 1 refers to vehicle 1 and 2 to vehicle 2"
        print "    - x and y inputs are in integers"
        print "    - face inputs are cardinal directions: N, S, E or W"
        print "    - movements are L, R, F, or B for a left turn, right turn, forward or back move. Ex: LFRB"

    def turn_left(self):
        self.face = directions[(directions.index(self.face)-1)%len(directions)]

    def turn_right(self):
        self.face = directions[(directions.index(self.face)+1)%len(directions)]

    def forward(self):
        new_x = self.x + movement[self.face][0]
        new_y = self.y + movement[self.face][1]

    def back(self):
        new_x = self.x + movement[self.face][-1]
        new_y = self.y + movement[self.face][0]

    def move(self,vehicle,movemt):
        """ This method does the main work of finding movement and returning new position """
        # 1. Check if vehicles overlap
        if abs(vehicle.x) > vehicle.max_x:
            vehicle.x = vehicle.max_x
        if abs(vehicle.y) > vehicle.max_y:
            vehicle.y = vehicle.max_y

        # 2. Assign movement based on command
        # 3. Return new position


if __name__ == '__main__':

    # Take input
    movement = Movement.input()
    max_x, max_y = map(int, raw_input().split())
    vehicle_one_pos = raw_input().split()
    vehicle_one_commands = raw_input()
    vehicle_two_pos = raw_input().split()
    vehicle_two_commands = raw_input()

    # Assign positions
    vehicle_one = Vehicle(int(vehicle_one_pos[0]), int(vehicle_one_pos[1]), vehicle_one_pos[2], max_x, max_y)
    vehicle_two = Vehicle(int(vehicle_two_pos[0]), int(vehicle_two_pos[1]), vehicle_two_pos[2], max_x, max_y)

    # Move vehicles
    for command in vehicle_one_commands:
        vehicle_one = movement.move(vehicle_one,command)

    for command in vehicle_two_commands:
        vehicle_two = movement.move(vehicle_two,command)

    # Return output
    print "Vehicle one's new position: (", vehicle_one.x,",", vehicle_one.y,"), facing ", vehicle_one.face
    print "Vehicle two's new position: (", vehicle_two.x,",", vehicle_two.y,"), facing ", vehicle_two.face