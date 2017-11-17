class Room(object):
    """Create a room object
    
    Each room is assumed to have four walls, with one possible door in each.
    Each wall will either have a door or not. No support for closed/open doors yet
    """

    def __init__(self, name, desc, north=True, east=True, south=True, west=True):
        self.name = name
        self.walls = {'north': north, 'south': south, 'east': east, 'west': west}
        self.desc = desc
    
    def welcome(self):
        print(f"You enter the {self.name} room")
        print(self.desc)
        for k, v in self.walls.items():
            if v:
                print(f"You see a door to the {k}")
    
fred = Room("Fred", "KITTIES!!!!!", north=False)

fred.welcome()