def flatten(iterable):
    flatenned_list = []
    
    # USING RECUSRION -->
    # if not isinstance(iterable, list):
    #     return [iterable] if iterable is not None else []
    # for item in iterable:
    #     if isinstance(item, list):
    #         flatenned_list.extend(flatten(item))
    #     elif item is not None:
    #         flatenned_list.append(item)
    # return flatenned_list


    # USING NORMAL APPROACH
    stack = list(iterable[::-1]) if isinstance(iterable, list) else [iterable]

    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])
        else:
            if item is not None:
                flatenned_list.append(item)
    return flatenned_list