# BRUTE FORCE (fails nesting and matching of brackets)
# def is_paired(input_string):
#     if count_of_brackets(input_string, '(') == count_of_brackets(input_string, ')') and count_of_brackets(input_string, '[') == count_of_brackets(input_string, ']') and count_of_brackets(input_string, '{') == count_of_brackets(input_string, '}'):
#         return True
#     return False
# def count_of_brackets(input_string, bracket):
#     count = 0
#     for char in input_string:
#         if char == bracket:
#             count+= 1
#     return count

def is_paired(input_string):
    stack = []
    
    # Map closing brackets to their matching opening brackets
    matching_bracket = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for char in input_string:
        # If it's an opening bracket, push it to the stack
        if char in matching_bracket.values():
            stack.append(char)
            
        # If it's a closing bracket
        elif char in matching_bracket:
            # It's unbalanced if there's no opening bracket to match it,
            # or if it doesn't match the most recent opening bracket
            if not stack or stack.pop() != matching_bracket[char]:
                return False
                
    # If the stack is empty, all brackets matched up perfectly
    return len(stack) == 0