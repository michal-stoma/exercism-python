def sieve(limit):
    numbers = [True] * (limit + 1)
    numbers[0] = numbers[1] = False

    for i in range(2, limit + 1):
        if numbers[i]:
            for j in range(i ** 2, limit + 1, i):
                numbers[j] = False

    return [i for i, v in enumerate(numbers) if v]