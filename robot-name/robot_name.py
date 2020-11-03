import string, random

class Robot:
    usednames = set([""])

    def __init__(self):
        self.name = self.newname()
    
    def reset(self):
        self.name = self.newname()

    def newname(self):
        name = ""
        while name in Robot.usednames:
            # Name schema: two random uppercase letters, three random digits
            name = random.choice(string.ascii_uppercase) \
                    + random.choice(string.ascii_uppercase) \
                    + str(random.randint(0,999)).zfill(3)
        Robot.usednames.add(name)
        return name
