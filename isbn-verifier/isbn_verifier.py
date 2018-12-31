def verify(isbn):

    isbn = isbn.replace('-', '')

    if len(isbn) != 10:
        return False

    if not isbn[-1].isdigit() and isbn[-1] != 'X':
        return False

    for i in isbn[:-1]:
        if not i.isdigit():
            return False

    check = sum((i + 1) * int(j) for i, j in enumerate(isbn[:-1])) % 11

    if check == 10:
        check = 'X'

    if str(check) == isbn[-1]:
        return True

    return False