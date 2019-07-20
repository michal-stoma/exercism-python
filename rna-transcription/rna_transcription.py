RNA_MAP = {
    'G': 'C',
    'T': 'A',
    'C': 'G',
    'A': 'U'
}


def to_rna(dna):
    rna = []

    for i in dna:
        rna.append(RNA_MAP[i])

    return ''.join(rna)
