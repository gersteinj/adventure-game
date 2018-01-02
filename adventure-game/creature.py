class Creature(object):
    """Base class for monster & character"""

    def __init__(self, name, strength):
        self.name = name
        self.hp = 100
        self.strength = strength
    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

