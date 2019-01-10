def is_armstrong(number):

    power = len(str(number))
    armstrong = int()

    for i in str(number):
        armstrong += (int(i) ** power)

    return number == armstrong
