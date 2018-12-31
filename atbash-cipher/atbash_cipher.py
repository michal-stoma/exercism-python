def _cipher(text):
    # Sum of ASCII codes of corresponding characters is 219,
    # e.g. ASCII for 'a' is 97, for replacing 'z' is 122,
    # for 'b' is 98 and for replacing 'y' is 121, and so on.
    # Subtracting character's code from 219 will give encoded character.
    # Additionally, if character is a digit (ASCII between 48 and 57),
    # we just append it. We drop other characters.

    _res = [chr(219 - ord(char)) if ord(char) in range(97, 123) else
            char if ord(char) in range(48, 58) else
            '' for char in text.lower()]

    # The same logic without list comprehensions:
    # res = []
    # for char in text.lower():
    #     if ord(char) in range(97, 123):
    #         res.append(chr(219 - ord(char)))
    #     elif ord(char) in range(48, 58):
    #         res.append(char)

    # Return an enocded/decoded string
    return ''.join(_res)


def encode(text):
    enc = _cipher(text)

    # Slice it into chunks no longer than 5 characters
    return ' '.join([enc[i:i + 5] for i in range(0, len(enc), 5)])


def decode(text):
    return _cipher(text)