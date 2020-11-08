def find_anagrams(word, candidates):
    chars = sorted(list(word.lower()))

    matches = []
    for c in candidates:
        if sorted(list(c.lower())) == chars and c.lower() != word.lower():
            matches.append(c)
    
    return matches
