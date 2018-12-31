def slices(digits, length):
    if len(digits) < length or length <= 0:
        raise ValueError

    return [[int(y) for x, y in enumerate(digits[i:i + length])]
            for i in range(len(digits) - length + 1)]