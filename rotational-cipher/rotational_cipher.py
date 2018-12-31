def rotate(string, key):
    _enc = [chr((ord(char) - 97 + key) % 26 + 97)
            if char.islower() and char.isalpha()
            else chr((ord(char) - 65 + key) % 26 + 65) if char.isalpha()
            else char
            for char in string]

    return ''.join(_enc)