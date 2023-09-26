def filter(the_list, start_filter=0):
    if (start_filter <= 0):
        return "You did not supply a valid filter number.  Please enter a positive integer."
    elif (start_filter >= len(the_list)):
        return the_list
    else:
        temp_list = []
        for i in range(start_filter):
            temp_list.append(the_list[i])
        return temp_list

    
list1 = list("Hello Operator, give me number nine.")
list2 = ['apple', 'banana', 'pear', 'grape', 'strawberry', 'blueberry', 'orange', 'pineapple', 'cherry', 'lemon']
# print(list1)
print(filter(list1, 12))
print(filter(list2, 7))
print(filter(list2, 21))
print(filter(list1, 3))
print(filter(list1, -1))