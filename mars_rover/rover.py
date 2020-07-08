from mars_rover.position import Position
from mars_rover.plateau import Plateau
from mars_rover.orientation import Orientation
from mars_rover.commands import Commands


class Rover(object):

    """
    This class has everything that rover.
    Rover's coordinates are initialised for the given plateau and which direction the rover is facing.
    Based on the commad that the Rover receives the rover can move by one unit or turn 90 degree right or left.
    In _rotation 90 degree is denotes as 1 unit thus Commands.RIGHT: 1 and Commands.LEFT:  -1.
    Assumption: the square directly North from (x, y) is (x, y+1). 
    """
 
    _directions = {Orientation.NORTH: (0, 1),
                   Orientation.EAST:  (1, 0),    
                   Orientation.SOUTH: (0, -1),
                   Orientation.WEST:  (-1, 0)}

    _rotation = {Commands.RIGHT: 1,
                 Commands.LEFT:  -1}


    def __init__(self, plateau, position, facing):
        """
        Initializing rover with following params:-
        :param plateau: Rectangular Area for the rover to travell. 
        :param position: x and y coordinates of the rover from Position class
        :param facing: The direction in which the rover is facing
        """
        self.plateau = plateau
        self.position = position
        self.facing = facing

    def __str__(self):
        return self.current_state()

    def set_facing(self, facing):
        self.facing = facing

    def set_position(self, x, y):
        if not isinstance(self.position, Position):
            self.position = Position(x, y)
        else:
            self.position.x = x
            self.position.y = y

    def current_state(self):
        return '{} {} {}'.format(self.position.x, self.position.y, self.facing.value)


    def begin_process(self, commands):
        for i in range(len(commands)):
            self.process_commands(commands[i])


    def process_commands(self, commands: [Commands]):
        for command in commands:
            if command == Commands.MOVE.value:
                self.move()
            elif command == Commands.RIGHT.value:
                self.turn(self._rotation[Commands.RIGHT])
            elif command == Commands.LEFT.value:
                self.turn(self._rotation[Commands.LEFT])
            else:
                print("Valid commands: L,R,M, Invalid Command entered: " , command)
                break


    def move(self):
        if not self.plateau.valid_move(self.position):
            print("Invalid Move")
            return 
        self.set_position(self.position.x+self._directions[self.facing][0], self.position.y+self._directions[self.facing][1] )


    def turn(self, ROTATE):
        directions = list(self._directions.keys())
        facing = directions[(directions.index(self.facing) + ROTATE)%len(directions)]
        self.set_facing(facing)


