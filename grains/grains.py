def square(number):
    if number < 1 or number > 64:
        raise ValueError('Number must be between 1 and 64')

# Worth remembering: bitwise operation are faster than power (2 ** n)
# but in case of such a small powers it's irrelevant.
    return 1 << (number - 1)


def total(number):
    if number < 1 or number > 64:
        raise ValueError('Number must be between 1 and 64')

    return (1 << number) - 1
