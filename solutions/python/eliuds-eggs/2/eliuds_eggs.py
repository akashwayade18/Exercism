def egg_count(display_value):
    # BRUTE FORCE
    # rev_binary_version = ''
    # while display_value > 0:
    #     rev_binary_version += str(display_value % 2)
    #     display_value = display_value // 2
    # binary_version = rev_binary_version[::-1]
    # count = 0
    # for i in binary_version:
    #     if i == '1':
    #         count += 1
    # return count

    # OPTIMIZED BRUTE FORCE
    # count = 0
    # while display_value > 0:
    #     if display_value % 2 == 1:
    #         count += 1
    #     display_value //= 2
    # return count

    # BITWISE VERSION
    # count = 0
    # while display_value > 0:
    #     count += display_value & 1
    #     display_value >>= 1
    # return count

    # Brian Kernighan’s Algorithm
    count = 0
    while display_value > 0:
        display_value &= display_value - 1
        count += 1
    return count
    
