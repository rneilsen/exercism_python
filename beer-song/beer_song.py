SPEC_VERSES = { 2: ['2 bottles of beer on the wall, 2 bottles of beer.',
                    'Take one down and pass it around, 1 bottle of beer on the wall.'],
                1: ['1 bottle of beer on the wall, 1 bottle of beer.',
                    'Take it down and pass it around, no more bottles of beer on the wall.'],
                0: ['No more bottles of beer on the wall, no more bottles of beer.',
                    'Go to the store and buy some more, 99 bottles of beer on the wall.']}

def recite(start, take=1):
    n = start
    response = []
    while take > 0:
        response += (SPEC_VERSES.get(n, 
                [f'{n} bottles of beer on the wall, {n} bottles of beer.',
                 f'Take one down and pass it around, {n-1} bottles of beer on the wall.']))
        take -= 1
        if take > 0: response += ['']
        n -= 1
        
    return response
