"""Exercism -> word-count."""
from collections import Counter


def word_count(string):
    """Count words in a given string. Return a dictionary."""
    def replace_nonalpha(char):
        return char.lower() if char.isalnum() else ' '

    string = ''.join(replace_nonalpha(c) for c in string)

    return Counter(string.split())