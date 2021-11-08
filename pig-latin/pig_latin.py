from string import ascii_lowercase

VOWEL_STARTS = {'a', 'e', 'i', 'o', 'u', 'xr', 'yt'}

def starts_with_vowel(text):
    for vowel_start in VOWEL_STARTS:
        if text.startswith(vowel_start):
            return True
    return False


def translate_word(word):
    if starts_with_vowel(word):
        return word + 'ay'

    consonants_to_move = ''
    while not starts_with_vowel(word):
        if word.startswith('qu'):
            consonants_to_move += 'qu'
            word = word[2:]
        elif word.startswith('y') and len(consonants_to_move) > 0:
            return word + consonants_to_move + 'ay'
        else:
            consonants_to_move += word[0]
            word = word[1:]

    return word + consonants_to_move + 'ay'


def translate(text):
    result = []
    for word in text.split():
        result.append(translate_word(word))

    return ' '.join(result)
