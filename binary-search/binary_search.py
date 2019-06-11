def binary_search(list_of_numbers, number):
    length = len(list_of_numbers)
    if length == 0:
        raise ValueError('Empty list to search in')

    if number < list_of_numbers[0] or number > list_of_numbers[-1]:
        raise ValueError('Value not found')

    found = None
    idx = length // 2

    # initial boundaries of a list (full list)
    start = 0
    end = length - 1

    while not found:
        if start > end:
            raise ValueError('Value not found')

        value = list_of_numbers[idx]

        if number == value:
            found = True

        elif number < value:
            # left side of array
            end = idx - 1

            # Make sure that idx will move by 1 at least. Using math.ceil()
            # instead of // could be another way to do that.
            idx_offset = (end - start) // 2 + 1
            idx -= idx_offset

        else:
            # right side of array
            start = idx + 1
            idx_offset = (end - start) // 2 + 1
            idx += idx_offset

    return idx
