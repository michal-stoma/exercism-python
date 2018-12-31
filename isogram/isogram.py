def is_isogram(string):
    _characters = [_char for _char in string.lower() if _char.isalpha()]
    return len(_characters) == len(set(_characters))