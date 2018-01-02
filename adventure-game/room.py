class Room(object):
    """Create a room object
    
    Each room is assumed to have four walls, with one possible door in each.
    Each wall will either have a door or not. No support for closed/open doors yet
    """

    def __init__(self, name, desc, north=False, east=False, south=False, west=False, contents = []):
        self.name = name
        self.doors = {'north': north, 'south': south, 'east': east, 'west': west}
        self.desc = desc
        self.contents = contents
    
    def welcome(self):
        print(f"You enter the {self.name} room")
        print(self.desc)
        for k, v in self.doors.items():
            if v:
                print(f"You see a door to the {k}")
        if len(self.contents) > 0:
            print('You see:')
            for content in self.contents:
                print(f" - {content}")

if __name__ == '__main__':

    print("""Whatever I put in this if statement will run if I'm running this code as the main program, but not if I'm importing it into something else""")