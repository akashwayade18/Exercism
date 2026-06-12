# def find(search_list, value):
#     low_index = 0
#     high_index = len(search_list) - 1
#     ans = -1
#     while (low_index <= high_index):
#         mid_index = (high_index + low_index) // 2
#         if search_list[mid_index] == value:
#             ans = mid_index
#             break
#         elif value > search_list[mid_index]:
#             low_index = mid_index + 1
#         else:
#             high_index = mid_index - 1
#     if ans == -1:
#         raise ValueError("value not in array")
#     else:
#         return ans

# USING RECURSION
def find(search_list, value):
    low = 0
    high = len(search_list) - 1
    ans = binary_search(search_list, value, low, high)
    if  ans == -1:
        raise ValueError("value not in array")
    else:
        return ans

def binary_search(search_list, value, low, high):
    if low > high:
        return -1
    mid = (high + low) // 2
    if search_list[mid] == value:
        return mid
    elif value > search_list[mid]:
        return binary_search(search_list, value, mid + 1, high)
    else:
        return binary_search(search_list, value, low, mid - 1)
    