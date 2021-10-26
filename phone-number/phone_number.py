class PhoneNumber:
    def __init__(self, number):
        scrubbed = ''.join([ch for ch in number if ch.isdigit()])
        if scrubbed[0] == '1':
            scrubbed = scrubbed[1:]
        
        if len(scrubbed) != 10:
            raise ValueError("NANP numbers must be 10 digits long")
        if int(scrubbed[0]) not in range(2,10):
            raise ValueError("Area code must start with digit 2-9")
        if int(scrubbed[3]) not in range(2,10):
            raise ValueError("Exchange code must start with digit 2-9")
        
        self.number = scrubbed
        self.area_code = scrubbed[:3]
    
    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"