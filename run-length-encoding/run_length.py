from itertools import groupby


def encode(data):
    groups = []
    for i, j in groupby(data):
        group_len = len(list(j))
        if group_len == 1:
            groups.append(i)
        else:
            groups.append(str(group_len) + i)

    return ''.join(groups)


def decode(data):
    decoded = ''
    index = 0

    while index < len(data):
        count = 0

        for char in data[index:]:
            if char.isdigit():
                count = 10 * count + int(char)
                index += 1
            else:
                if count == 0:
                    decoded += char
                else:
                    decoded += count * char
                index += 1
                break

    return decoded