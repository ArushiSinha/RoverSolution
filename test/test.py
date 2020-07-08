import unittest
from mars_rover.position import Position
from mars_rover.plateau import Plateau
from mars_rover.orientation import Orientation
from mars_rover.commands import Commands
from mars_rover.rover import Rover

class RoverTest(unittest.TestCase):
    def test_constructor(self):
        plateau = Plateau(3, 7)
        position = Position(0, 0)
        rover = Rover(plateau, position, Orientation.NORTH)
        self.assertEqual(Position(0, 0), rover.position)
        self.assertEqual(plateau, rover.plateau)

    def test_move(self):
        plateau = Plateau(3, 7)
        position = Position(0, 0)
        rover = Rover(plateau, position, Orientation.NORTH)
        _directions = {Orientation.NORTH: (0, 1),
                   Orientation.EAST:  (1, 0),    
                   Orientation.SOUTH: (0, -1),
                   Orientation.WEST:  (-1, 0)}
        rover.move()
        self.assertEqual(Position(0, 1), rover.position)

    def test_turn(self):
        plateau = Plateau(3, 7)
        position = Position(0, 0)
        rover = Rover(plateau, position, Orientation.NORTH)
        _rotation = {Commands.RIGHT: 1,
                 Commands.LEFT:  -1}
        ROTATE = _rotation[Commands.LEFT]
        rover.turn(ROTATE)
        self.assertEqual('W', rover.facing.value)

class TestPosition(unittest.TestCase):
    def testConstructor(self):
        position = Position()
        self.assertEqual(position.x, 0)
        self.assertEqual(position.y, 0)

        position = Position(5, 8)
        self.assertEqual(position.x, 5)
        self.assertEqual(position.y, 8)


class TestPlateau(unittest.TestCase):
    def testConstructor(self):
        plateau = Plateau(2, 8)
        self.assertEqual(plateau.width, 2)
        self.assertEqual(plateau.height, 8)



if __name__ == '__main__':
    unittest.main()