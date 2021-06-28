from re import findall

PAIRS = ['()', '[]', '{}']

def is_paired(input_string):
    # build a dict of brackets: key = opening symbol, value = closing symbol
    brackets = {}
    for p in PAIRS:
        brackets[p[0]] = p[1]
    
    # constructs a list of all recognised brackets in order from input_string
    pattern = ''.join(['\\' + c for c in (''.join(PAIRS))])
    bracket_list = findall('[' + pattern + ']', input_string)
    
    if len(bracket_list) % 2 != 0:
        return False
    
    # iterate through bracket_list checking if brackets close correctly
    found_openers = []
    for b in bracket_list:
        if b in brackets.keys():
            found_openers.append(b)
        else:
            if len(found_openers) < 1 or brackets[found_openers.pop()] != b:
                return False
    
    # check if any unclosed brackets remain
    if len(found_openers) > 0:
        return False
    
    return True
