def transpose(text):
    if not text:
        return ''
    rows = text.split('\n')
    num_rows = len(rows)
    max_cols = max(len(row) for row in rows)
    transposed_rows = []
    
    for c in range(max_cols):
        current_transposed_row = []
        for r in range(num_rows):
            if c < len(rows[r]):
                current_transposed_row.append(rows[r][c])
            else:
                has_character_below = False
                for i in range(r+1, num_rows):
                    if c < len(rows[i]):
                        has_character_below = True
                        break
                if has_character_below:
                    current_transposed_row.append(' ')
        transposed_rows.append(''.join(current_transposed_row))
    return '\n'.join(transposed_rows)
