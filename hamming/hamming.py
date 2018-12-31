"""Exercism -> hamming."""


def distance(dna1, dna2):
    """Calculate Hamming distance for two give DNA strands."""
    if len(dna1) != len(dna2):
        raise ValueError

    count = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            count += 1

    return count