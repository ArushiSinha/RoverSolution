class Plateau(object):
    """
    This class defines the plateau region for the rover.
    The region is assumed to be rectangular with min width and min height as 0
    """
    MIN_WIDTH = 0
    MIN_HEIGHT = 0

    def __init__(self, width, height, min_width=0, min_height=0):
        self.width = width
        self.height = height
        self.MIN_WIDTH = min_width
        self.MIN_HEIGHT = min_height

    def valid_move(self, position):
        """
        Position coordinates is inside the rectangular Plateave region 
        """
        return self.MIN_WIDTH <= position.x <= self.width and self.MIN_HEIGHT <= position.y <= self.height