def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    distance = 0
    length = len(strand_a)
    for i in range( length):
        if strand_a[i] != strand_b[i]:
            distance += 1
    return distance
