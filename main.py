from mars_rover.position import Position
from mars_rover.plateau import Plateau
from mars_rover.rover import Rover
from mars_rover.orientation import Orientation

def main():
    """
    The entrypoint of the code. It reads the input file and creates rover objects.
    Each rover will be finished sequentially, which means that the second rover won’t start to
    move until the first one has finished moving.
    The input file format: 
    5 5 
    1 2 N LMLMLMLMM
    3 3 E MMRMMRMRRM

    Line 1: Plateau hight and width
    Each line after that defines rover [x-position y-position direction(N,S,E,W) Commands(L,R,M)] 
    """
    try:
        with open("input.txt") as fp:
            plateau_line = fp.readline()
            plateau_x, plateau_y = plateau_line.split()
            plateau = Plateau(int(plateau_x), int(plateau_y))
            Lines = fp.readlines() 
            for line in Lines:
                (x, y, facing, commands) = line.split()
                position = Position(int(x), int(y))
                rover = Rover(plateau, position, Orientation(facing.upper()))
                rover.begin_process(commands.upper())
                print(rover)
    except FileNotFoundError:
        print("Wrong file path or name")
    except ValueError:
        print("This error could be due to wrong values in the input file, missing values or invalid input format. Please check valid input format from README.md")



if __name__ == "__main__":
    main()