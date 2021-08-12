names = { 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

powers = {0: '', 3: ' thousand', 6: ' million', 9: ' billion'}

# construct 'names' dict for all numbers up to 1000
for n in range(21, 100): 
    if n not in names:
        names[n] = names[10 * (n//10)] + '-' + names[n % 10]

for n in range(10):
    names[100*n] = names[n] + ' hundred'

for n in range(100, 1000):
    if n not in names:
        names[n] = names[100 * (n//100)] + ' ' + names[n % 100]


def say(number):
    if not (0 <= number < 10**12): raise ValueError("Number out of range")

    if number == 0: return 'zero'
    
    parts = []
    
    for p in powers.keys():
        block = number % 1000
        if block > 0:
            parts.append(names[block] + powers[p])
        number = number // 1000
    
    parts.reverse()
    return ' '.join(parts)
