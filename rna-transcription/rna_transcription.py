def to_rna(dna_strand, out="", asd=["G", "C", "T", "A"], dsa=["C", "G", "A", "U"]):
    for acid in dna_strand:
        out = out + dsa[asd.index(acid)]
    return out
