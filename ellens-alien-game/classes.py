"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    y_coordinate,x_coordinate,health,total_aliens_created=0,0,3,0
    def teleport(self,x_coord,y_coord):
        self.x_coordinate,self.y_coordinate = x_coord,y_coord
    def __init__(self, x_coord,y_coord):
        self.teleport(x_coord,y_coord)
        self.health = 3
        Alien.total_aliens_created +=1

    def hit(self):
        self.health -= 1
    is_alive = lambda self: self.health > 0
    def collision_detection(self, obj):
        pass
new_aliens_collection = lambda start_positions: (Alien(*pos) for pos in start_positions)
#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
