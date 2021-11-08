MAPPING = { 'G': 'C' ,
            'C': 'G' ,
            'T': 'A' ,
            'A': 'U' }

def to_rna(dna_strand):
    return ''.join([MAPPING[ch] for ch in dna_strand])
