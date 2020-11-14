# Allergen values and corresponding powers of two 
# (e.g. 'chocolate' corresponds to 2^5 = 32)
# Note: module will work even if some allergen/powers of 2 are missing
VALS = {0: 'eggs', 
        1: 'peanuts',
        2: 'shellfish',
        3: 'strawberries',
        4: 'tomatoes',
        5: 'chocolate',
        6: 'pollen',
        7: 'cats'}

class Allergies:

    def __init__(self, score):
        # find first power of 2 larger than score
        n = 0
        while score >= 2**n:
            n += 1
        
        # subtract all powers of 2 in descending order, and note allergies
        self.allergies = []
        while n >= 0:
            if score >= 2**n:
                score = score - 2**n
                if n in VALS:
                    self.allergies.append(VALS[n])
            n = n-1

    def allergic_to(self, item):
        return (item in self.allergies)

    @property
    def lst(self):
        return self.allergies
