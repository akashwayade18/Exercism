def to_rna(dna_strand):
    re_dna = ""
    for char in dna_strand:
        if char == 'G':
            re_dna += 'C'
        elif char == 'C':
            re_dna += 'G'
        elif char == 'A':
            re_dna += 'U'
        else:
            re_dna += 'A'
    return re_dna