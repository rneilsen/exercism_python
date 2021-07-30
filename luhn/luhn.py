class Luhn:
    def __init__(self, card_num):
        self.num = card_num
        
    def valid(self):
        digits = []
        for ch in self.num:
            if ch.isdigit():
                digits.append(int(ch))
            elif ch != ' ':
                return False
        if len(digits) <= 1:
            return False
        
        def rec_luhn_sum(digits):
            if len(digits) < 2:
                return sum(digits)
            return (digits[-1] + 2*digits[-2] - (9 if digits[-2] >= 5 else 0) +
                    rec_luhn_sum(digits[:len(digits) - 2]))        

        return (rec_luhn_sum(digits) % 10 == 0)