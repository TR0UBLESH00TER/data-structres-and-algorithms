class robot:
    """Classic example of robot class for the classes"""
    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model
    
    def info(self):
        """Returns bot's information in the form of a dictionary. """
        return {'name':self.name, 'color':self.color, 'model':self.model}

r1 = robot('Beep', 'Blue', 'alpha0.5')
r2 = robot('Boop', 'Grey', 'alpha1.5')

print(r1, r2, sep = "\n")
print()
print(r1.info(), r2.info(), sep = "\n")