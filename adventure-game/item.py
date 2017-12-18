class Item(object):

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    
    def __str__(self):
        return str(self.name)