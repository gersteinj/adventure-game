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

    # room_names = [
    #     ['a', 'b', 'c', 'd', 'e'],
    #     ['f', 'g', 'h', 'i', 'j'],
    #     ['k', 'l', 'm', 'n', 'o'],
    #     ['p', 'q', 'r', 's', 't'],
    #     ['u', 'v', 'w', 'x', 'y']
    # ]

    room_names = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]

    dungeon_map = []
    for x in range(3):
        row = []
        for y in range(3):
            row.append(Room(f"{room_names[x][y]} - {x},{y}", '.'))
        dungeon_map.append(row)

    for row in dungeon_map:
        for room in row:
            print(room.name)
            room.welcome()