# Add overall comment describing the code
# State Python version used, author coordinates
# Write unit tests and try/except error handling
# User inputs should be defined/prompted for with description
# User inputs should be grouped together in the code
# Typo in vehicle_two below
# Write code in methods, avoid global variables. Don't reference global variables inside the class
# dir could be a protected variable (for directory), should avoid

directions = ['N','E','S','W']
movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}
commands = {'L': 'turn_left', 'R': 'turn_right', 'M': 'move'}

GRID_MAX_X, GRID_MAX_Y = map(int, raw_input().split())

# These are not used effectively
first_vehicle_x = None
first_vehicle_y = None

class Vehicle():
    def __init__(self, x, y, face):
        self.x = x
        self.y = y
        self.dir = face

    # Seems to me like movements would make more sense as a separate class
    def turn_left(self):
        self.dir = directions[(directions.index(self.dir)-1)%len(directions)]

    def turn_right(self):
        self.dir = directions[(directions.index(self.dir)+1)%len(directions)]

    def move(self):
        new_x = self.x + movement[self.dir][0]
        new_y = self.y + movement[self.dir][1]

        # This if condition doesn't do anything ?
        if new_x != first_vehicle_x or new_y != first_vehicle_y:
            if new_x in xrange(GRID_MAX_X+1):
                self.x = new_x
            if new_y in xrange(GRID_MAX_Y+1):
                self.y = new_y

vehicle_one_pos = raw_input().split()
vehicle_one_commands = raw_input()

vehicle_one = Vehicle(int(vehicle_one_pos[0]), int(vehicle_one_pos[1]), vehicle_one_pos[2])
for command in vehicle_one_commands:
    # better to write as method call rather than eval - eval is slower and more command-line centric
    eval("vehicle_one.{0}()".format(commands[command]))

# These definitions do not persist so are not actually used
first_vehicle_x = vehicle_one.x
first_vehicle_y = vehicle_one.y


vehicle_two_pos = raw_input().split()
vehicle_two_commands = raw_input()

# Typo: should be vehicle_two_pos
vehicle_two = Vehicle(int(vehicle_two_pos[0]), int(vehicle_two_pos[1]), vehicle_two_pos[2])
for command in vehicle_two_commands:
    eval("vehicle_two.{0}()".format(commands[command]))

print vehicle_one.x, vehicle_one.y, vehicle_one.dir
print vehicle_two.x, vehicle_two.y, vehicle_two.dir
