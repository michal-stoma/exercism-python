RNA_MAP = str.maketrans('GTCA', 'CAGU')


def to_rna(dna):
    return dna.translate(RNA_MAP)
