import string, random

class Robot:
    used_names = set()

    def __init__(self):
        self.name = Robot.newname()
    
    def reset(self):
        self.name = Robot.newname()

    @staticmethod
    def newname():
        cont = True
        while cont:
            # Name schema: two random uppercase letters, three random digits
            name = ''.join(random.choices(string.ascii_uppercase, k=2)) \
                    + str(random.randint(0,999)).zfill(3)
            if name not in Robot.used_names:
                cont = False
        Robot.used_names.add(name)
        return name
