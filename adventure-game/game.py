from character import Character


class Monster(object):
    """Create a monster object"""

    def __init__(self, name, health, strength, defense, desc):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.desc = desc
    
jen = Character('Jen')

print(dir(jen))

print(jen.name)