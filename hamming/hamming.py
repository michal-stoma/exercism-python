def distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError('Strands have to be of equal length!')

    return sum(map(lambda x, y: x != y, dna1, dna2))
