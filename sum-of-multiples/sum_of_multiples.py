def sum_of_multiples(limit, factors):
    # For every factor different than 0, generate factor's multiples using
    # range expression with step = factor. Add multiples to a set, to eliminate
    # duplicates.
    result = set()
    for factor in factors:
        if factor:
            for i in range(0, limit, factor):
                result.add(i)
    return sum(result)