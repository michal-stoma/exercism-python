import string

ALPHABET = string.ascii_lowercase


def is_pangram(s):
    return not any([char not in s.lower() for char in ALPHABET])