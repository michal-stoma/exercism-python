"""Exercism -> rna-transcription."""


def to_rna(dna):
    """Return RNA for provided DNA."""
    if not all(i in 'GCTA' for i in dna):
        return ''

    rna = []
    for i in range(len(dna)):
        if dna[i] == 'G' or dna[i] == 'T':
            rna.append(dna[i].replace('G', 'C').replace('T', 'A'))
        else:
            rna.append(dna[i].replace('C', 'G').replace('A', 'U'))
    return ''.join(rna)