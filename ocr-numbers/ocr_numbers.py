# Create a dict (DIGITS): key = each digit as pipes and underscores, val = str(integer)
RAW_DIGITS = '''
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
                              '''
DIGITS = {}
for n in range(10):
    digit_rows = [row[3*n:3*n+3] for row in RAW_DIGITS.splitlines()[1:]]
    DIGITS['\n'.join(digit_rows)] = str(n)

def convert(input_grid):
    if len(input_grid) < 4: 
        raise ValueError("Input does not have at least 4 rows")
    if len(input_grid) % 4 != 0:
        raise ValueError("Input does not have multiple of 4 rows")
        
    result = ''
    for n in range(0, len(input_grid), 4):
        big_row = input_grid[n:n+4]

        # check all lines in this big_row are same mult-of-3 length
        lengths = [len(line) for line in big_row]
        if len(set(lengths)) != 1:
            raise ValueError("Rows in a set of 4 not the same length")
        if lengths[0] % 3 != 0:
            raise ValueError("Rows are not multiple-of-three in length")

        # peel off each big_digit in big_row and identify
        for i in range(0, len(big_row[0]), 3):
            big_digit = [big_row[n][i:i+3] for n in range(4)]
            result += DIGITS.get('\n'.join(big_digit), '?')
        
        result += ','
    
    result = result[:-1]    # strip final comma
    
    return result
