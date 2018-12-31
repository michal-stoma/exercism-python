"""Exercism -> bob."""


def hey(what):
    """Return Bob's answer."""
    if what.isupper():
        return 'Whoa, chill out!'

    if what.rstrip(' ').endswith('?'):
        return 'Sure.'

    if what.isspace() or not what:
        return 'Fine. Be that way!'

    return 'Whatever.'