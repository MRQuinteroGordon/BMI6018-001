def traverse_nest(input_list):
    if not isinstance(input_list, list):    #if argument was not a list:
        return "The input is not a list. Try again."
    
    if not input_list:      #if list was not supplied when function called:
        return "The input list is empty."
    
    def is_valid(element):  #function for verifying an element of a list is an integer or nested list
        return isinstance(element, (int, list))
    
    deepest_list = None 
    max_depth = -1
    stack = [(input_list, 0)]  # This list will be a stack with root list and its depth 0 contained in a tuple
    
    while stack:        #while the stack list is not empty
        current_list, depth = stack.pop()  # Pop a list and its depth from the stack and unpack it into current_list and depth variables

        # If at least one of the items is invalid after going through each item in the list
        if any(not is_valid(item) for item in current_list):
            # Return error message
            return "There is an invalid item in the list. Only integers and lists are valid items. Try again."

        if depth > max_depth:  # Update deepest_list and max_depth
            deepest_list = current_list
            max_depth = depth
        
        idx = len(current_list) - 1
        while idx >= 0:  # Process each item in the current list
            if isinstance(current_list[idx], list):     #if item is a list:
                stack.append((current_list[idx], depth + 1))  # Push each nested list and its depth to the stack
            idx -= 1
    
    if deepest_list is not None:    #if a nested list was found, deepest list will be in deepest_list:
        idx = len(deepest_list) - 1
        while idx >= 0:  # Increment each element in the deepest list by 1
            deepest_list[idx] += 1
            idx -= 1
    
    return input_list

# Main
list1 = [[3, 7], 12, 31, 6, [1, [1, 2, 3, [87, [45, 56]]]]]
list1a = [[3, 7], 12, 31, 6, [1, [1, 2, 3, [87, [45, [56, 80]]]]]]
list2 = [9, 8, [2, [3, 1]], 7, [1, 12]]
list2a = [9, 8, [2, [3, [1, [2, 8]]]], 7, [1, 12]]
list3 = []
list4 = [1, ["hello", 3]]
list5 = 3

print(traverse_nest(list1))  # [[3, 7], 12, 31, 6, [1, [1, 2, 3, [87, [46, 57]]]]]
print(traverse_nest(list1a))  # [[3, 7], 12, 31, 6, [1, [1, 2, 3, [87, [45, [57, 81]]]]]]
print(traverse_nest(list2))  # [9, 8, [2, [4, 2]], 7, [1, 12]]
print(traverse_nest(list2a))  # [9, 8, [2, [3, [1, [3, 9]]]], 7, [1, 12]]
print(traverse_nest(list3))  # The input list is empty.
print(traverse_nest(list4))  # Invalid item in the list: hello
print(traverse_nest(list5))  # The input is not a list. Try again.
