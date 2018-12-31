from functools import reduce


def largest_product(digits, span):
    if span < 0:
        raise ValueError

    return max(reduce((lambda x, y: x * y), map(int, digits[i:i + span]), 1)
               for i in range(0, len(digits) - span + 1))