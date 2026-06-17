def slices(series, length):
    series_length = len(series)
    for_range = series_length - length + 1
    if length == 0:
        raise ValueError("slice length cannot be zero")
    elif length < 0:
        raise ValueError("slice length cannot be negative")
    elif not series:
        raise ValueError("series cannot be empty")
    elif length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    else:
        result = []
        for i in range(0, for_range):
            result.append(series[i : i + length])
        return result
