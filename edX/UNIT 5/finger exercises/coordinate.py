class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        # return f"{self.x}, {self.y}"
        # return f"{self.getX()}, {self.getY()}"
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self):
        return self.getX() == self.getY()
    
    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self.getX() == other.getX() and self.getY() == other.getY()
        return False
    
    def __repr__(self):
        return f'Coordinate({self.getX()}, {self.getY()})'

    def __repr__(self):
        return f'Coordinate({self.x}, {self.y})'
        # return f'Coordinate({self.getX()}, {self.getY()})'
    
    
instance = Coordinate(0, 1)
print(instance) 