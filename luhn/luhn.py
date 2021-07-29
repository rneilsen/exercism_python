class Luhn:
    def __init__(self, card_num):
        self.num = card_num
        
    def valid(self):
        chars = list(self.num.strip().replace(' ', ''))
        if len(chars) <= 1:
            return False
        for ch in chars:
            if not ch.isdigit(): return False

        digits = [int(ch) for ch in chars]
        digits.reverse()

        norm_digits = digits[::2]
        doub_digits = [(2*d - 9 if d >= 5 else 2*d) for d in digits[1::2]]
        return (sum(norm_digits + doub_digits) % 10 == 0)
