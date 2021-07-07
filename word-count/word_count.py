from collections import Counter
import re

def count_words(sentence):
    word_list = re.findall("[0-9a-z]+(?:'[a-z]+)?", sentence.strip().lower())
    word_counts = Counter(word_list)
    return word_counts