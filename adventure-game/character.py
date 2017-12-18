from item import Item
import item_library

class Character(object):
    """Character class. Template for creating a character.

    I don't expect to have multiple characters, but this will still let me organize my main file better."""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = [item_library.armor, item_library.sword, item_library.apple, item_library.apple]
        self.money = 50
    
    def show_inventory(self):
        print('Inventory:')
        for item in self.inventory:
            print(f" - {item}")

    def is_healthy(self):
        if self.health <= 0:
            return False
        else:
            return True

    def show_health(self):
        print(f"Health: {self.health}/100")

    def show_status(self):
        print(f"Character: {self.name}")
        self.show_health()
        self.show_inventory()
        
    def take_damage(self, hit=1):
        self.health -= hit
        print(f"You took {hit} damage.")
        if self.is_healthy():
            print("You're still okay.")
        else:
            print("That's a problem...")
    
    def eat(self, thing_to_eat):
        if thing_to_eat.category == 'food':
            self.health += 1
            print(f"You ate the {thing_to_eat} and healed by 1")
        else:
            print(f"You can't eat that {thing_to_eat}.")
    
    def __str__(self):
        """By modifying the __str__ function, I can print the object and get a human-readable name"""
        return str(self.name)

if __name__ == '__main__':
    jen = Character('Jen')

    jen.show_status()
    jen.take_damage(5)
    jen.show_health()
    for item in jen.inventory:
        jen.eat(item)
        jen.show_health()