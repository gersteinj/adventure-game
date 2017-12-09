class Character(object):

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = {
            'leather boots': 1,
            'pants': 1,
            'shirt': 1
        }
    
    def show_inventory(self):
        for item, qty in self.inventory.items():
            print(f" - {item}: {qty}")

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
    
if __name__ == '__main__':
    jen = Character('Jen')

    jen.show_status()
    jen.take_damage(5)
    jen.show_health()