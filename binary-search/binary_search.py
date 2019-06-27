def binary_search(list_of_numbers, number):
    length = len(list_of_numbers)
    if length == 0:
        raise ValueError('Empty list to search in')

    if number < list_of_numbers[0] or number > list_of_numbers[-1]:
        raise ValueError('Value not found')

    found = None

    # initial boundaries of a list (full list)
    start = 0
    end = length - 1

    while not found:
        idx = (start + end) // 2

        if start > end:
            raise ValueError('Value not found')

        value = list_of_numbers[idx]

        if number == value:
            found = True

        elif number < value:
            # left side of array
            end = idx - 1

        else:
            # right side of array
            start = idx + 1

    return idx
