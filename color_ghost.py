import random
class Ghost(object):
    def __init__(self):
        color = ['white', 'yellow', 'purple', 'red']
        self.color = random.choice(color)