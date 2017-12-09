class Room(object):
    """Create a room object
    
    Each room is assumed to have four walls, with one possible door in each.
    Each wall will either have a door or not. No support for closed/open doors yet
    """

    def __init__(self, name, desc, north=True, east=True, south=True, west=True, contents = []):
        self.name = name
        self.walls = {'north': north, 'south': south, 'east': east, 'west': west}
        self.desc = desc
        self.contents = contents
    
    def welcome(self):
        print(f"You enter the {self.name} room")
        print(self.desc)
        for k, v in self.walls.items():
            if v:
                print(f"You see a door to the {k}")
        if len(self.contents) > 0:
            print('You see:')
            for content in self.contents:
                print(f" - {content}")

class Monster(object):
    """Create a monster object"""

    def __init__(self, name, health, strength, defense, desc):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.desc = desc
    
fred = Room("Fred", "KITTIES!!!!!", north=False, contents = ['fred', 'maurice', 'aaron purr'])

fred.welcome()