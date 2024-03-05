import re
from collections import Counter

def create_vocabulary_dict(corpus_file):
    """Create a dictionary of English vocabulary from the given corpus file."""
    vocabulary_dict = Counter()
    with open(corpus_file, 'r', encoding='utf-8') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())
            vocabulary_dict.update(words)
    return vocabulary_dict

def spelling_checker(misspelled_word, vocabulary_dict):
    """Check spelling of a word and return a list of five most likely corrected words."""
    candidates = []
    for word in vocabulary_dict:
        if len(word) == len(misspelled_word):
            distance = sum(1 for a, b in zip(word, misspelled_word) if a != b)
            candidates.append((word, distance))
    candidates.sort(key=lambda x: x[1])
    corrected_words = [candidate[0] for candidate in candidates[:5]]
    return corrected_words

# # Example usage:
# corpus_file = 'books\Anna_Karenina_by_Leo_Tolstoy.rtf'  # Replace the path to your corpus file
# vocabulary_dict = create_vocabulary_dict(corpus_file)

# #misspelled_word = 'teh'
# misspelled_word = input("Enter a word: ")
# corrected_words = spelling_checker(misspelled_word, vocabulary_dict)
# print("Corrected words for '{}' are:".format(misspelled_word), corrected_words)