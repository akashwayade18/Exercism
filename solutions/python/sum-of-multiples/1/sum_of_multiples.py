def sum_of_multiples(limit, multiples):
    # BRUTE FORCE
    # multiples_set = set()
    # for item in multiples:
    #     for i in range(item, limit):
    #         if item > 0 and i % item == 0:
    #             multiples_set.add(i)
    # return sum(i for i in multiples_set)

    # OPTIMAL
    # multiples_set = set()
    # for item in multiples:
    #     if item == 0:
    #         continue
    #     for i in range(item, limit, item):
    #         multiples_set.add(i)
    # return sum(i for i in multiples_set)

    # COMPREHENSION
    return sum({x for i in multiples if i > 0 for x in range(i, limit, i)})
            
