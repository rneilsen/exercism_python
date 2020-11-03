import string, random

class Robot:
    usednames = set([""])

    def __init__(self):
        self.name = Robot.newname()
    
    def reset(self):
        self.name = Robot.newname()

    @staticmethod
    def newname():
        name = ""
        while name in Robot.usednames:
            # Name schema: two random uppercase letters, three random digits
            name = random.choice(string.ascii_uppercase) \
                    + random.choice(string.ascii_uppercase) \
                    + str(random.randint(0,999)).zfill(3)
        Robot.usednames.add(name)
        return name
