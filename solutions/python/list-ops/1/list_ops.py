def append(list1, list2):
    result = []
    for item in list1:
        result += [item]
    for item in list2:
        result += [item]
    return result

    # return list1 + list2

def concat(lists):
    result = []
    for sublist in lists:
        result = append(result, sublist)
    return result

def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result += [item]
    return result

def length(list):
    count = 0
    for i in list:
        count += 1
    return count

def map(function, list):
    result = []
    for item in list:
        result += [function(item)]
    return result

def foldl(function, list, initial):
    acc = initial
    for item in list:
        acc = function(acc, item)
    return acc


def foldr(function, list, initial):
    acc = initial
    for item in reverse(list):
        acc = function(acc, item)
    return acc

    
def reverse(list):
    result = []
    for item in list:
        result = [item] + result
    return result