CODON_TABLE = {'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine', 'UUA': 'Leucine', 'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan', 'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'}

def proteins(strand):
    # BRUTE FORCE
    # amino_acid = []
    # for i in range(0, len(strand), 3):
    #     current_codon = strand[i : i+3]
    #     if current_codon == 'AUG':
    #         amino_acid.append('Methionine')
    #     elif current_codon in ['UUU', 'UUC']:
    #         amino_acid.append('Phenylalanine')
    #     elif current_codon in ['UUA', 'UUG']:
    #         amino_acid.append('Leucine')
    #     elif current_codon in ['UCU', 'UCC', 'UCA', 'UCG']:
    #         amino_acid.append('Serine')
    #     elif current_codon in ['UAU', 'UAC']:
    #         amino_acid.append('Tyrosine')
    #     elif current_codon in ['UGU', 'UGC']:
    #         amino_acid.append('Cysteine')
    #     elif current_codon == 'UGG':
    #         amino_acid.append('Tryptophan')
    #     elif current_codon in ['UAA', 'UAG', 'UGA']:
    #         break
    # return amino_acid

    # OPTIMAL SOLUTION
    length = len(strand)
    amino_acids = []
    for i in range(0, length, 3):
        current_codon = strand[i : i+3]
        if len(current_codon) < 3:
            break
        protein = CODON_TABLE.get(current_codon)
        if protein == 'STOP':
            break
        if protein:
            amino_acids.append(protein)
    return amino_acids
        