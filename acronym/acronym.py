from re import findall


def abbreviate(phrase):
    regex = '[A-Z]+[a-z]*|[a-z]+'
    return ''.join([c[0].upper() for c in findall(regex, phrase)])