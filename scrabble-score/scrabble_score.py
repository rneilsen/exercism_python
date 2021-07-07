score_groups = {
        1:  'aeioulnrst',
        2:  'dg',
        3:  'bcmp',
        4:  'fhvwy',
        5:  'k',
        8:  'jx',
        10: 'qz'
    }

# builds a dict of per-letter scores from the above human-convenient score list
scores = {}
for score_value in score_groups.keys():
    for letter in score_groups[score_value]:
        scores[letter] = score_value

def score(word):
    return sum([scores[l] for l in word.lower()])
