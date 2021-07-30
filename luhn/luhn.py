class Luhn:
    def __init__(self, card_num):
        self.num = card_num
        
    def valid(self):
        chars = list(self.num.strip().replace(' ', ''))
        
        if len(chars) <= 1:
            return False
        for ch in chars:
            if not ch.isdigit(): return False

        def rec_luhn_sum(digits):
            if len(digits) < 2:
                return sum(digits)
            return (digits[-1] + 2*digits[-2] - (9 if digits[-2] >= 5 else 0) +
                    rec_luhn_sum(digits[:len(digits) - 2]))        

        digits = [int(ch) for ch in chars]
        return (rec_luhn_sum(digits) % 10 == 0)