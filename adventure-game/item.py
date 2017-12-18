class Item(object):
    """Item class. Template for creating objects to be used in game.
    
    Subclasses for each category might be implemented later."""

    def __init__(self, name, description, value, category='general'):
        """Defined categories so far: general, food, weapon"""
        self.name = name
        self.description = description
        self.value = value
        self.category = category

    def __str__(self):
        """By modifying the __str__ function, I can print the object and get a human-readable name"""
        return str(self.name)