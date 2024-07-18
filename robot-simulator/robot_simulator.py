# Globals for the directions
# Change the values as you see fit
#Δx, Δy, left, right
EAST,NORTH,WEST,SOUTH = [1,0,0,2],[0,1,1,3],[-1,0,2,0],[0,-1,3,1]
directions = [NORTH,WEST,SOUTH,EAST]# if python were lazy we could define globals in terms of each other


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction, self.coordinates = direction, (x_pos,y_pos)
    def move(self,commands):
        for com in commands:
            if com=="A": self.__init__(self.direction, self.coordinates[0] + self.direction[0], self.coordinates[1] + self.direction[1])
            if com=="L": self.__init__(directions[self.direction[2]], self.coordinates[0],self.coordinates[1])
            if com=="R": self.__init__(directions[self.direction[3]], self.coordinates[0],self.coordinates[1])
