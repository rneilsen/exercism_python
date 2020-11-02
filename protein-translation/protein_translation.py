# NOTE: Add amino acids and codons here
AMINO_ACIDS = {
    "Methionine":       ["AUG"],
    "Phenylalanine":    ["UUU", "UUC"],
    "Leucine":          ["UUA", "UUG"],
    "Serine":           ["UCU", "UCC", "UCA", "UCG"],
    "Tyrosine":         ["UAU", "UAC"],
    "Cysteine":         ["UGU", "UGC"],
    "Tryptophan":       ["UGG"],
    "STOP":             ["UAA", "UAG", "UGA"]
}

def proteins(strand):
    codons = {}
    # build codons dict from AMINO_ACIDS for codon-based lookup
    for amino in AMINO_ACIDS.keys():
        for c in AMINO_ACIDS[amino]:
            codons[c] = amino
    
    # parse strand by codons and create list of amino acids
    output = []
    for c in [strand[i:i+3] for i in range(0, len(strand), 3)]:
        if codons[c] == "STOP":
            break
        else:
            output.append(codons[c])
    
    return(output)
