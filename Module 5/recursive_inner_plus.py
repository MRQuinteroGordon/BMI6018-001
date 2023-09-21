list1 = [[3, 7], 12, 31, 6, [1, [1, 2, 3, [87, [45, 56]]]]]
list2 = [9, 8, [2, [3, 1]], 7, [1, 12]]
list3 = []
list4 = [1, "hello", 3]
list5 = 3
length = 0


def traverse_nest(nestlist):
    global length
    
    #check to make sure a list was passed in
    if not isinstance(nestlist, list):
        print("That is not a list.  Try again.")
        return
    #if list passed into function is empty
    if len(nestlist) == 0:
        print("List is empty.")
        return
    else:
        #iterate through list
        for element in nestlist:
            #check it is a valid data type
            if not isinstance(element, (int, list)):
                print("The element is not an integer or list.  Lists can only contain integers or other lists.  Try again.")
                return
            #check if element at this index is a nested list
            print(element, "is a ", type(element))
            #if it is a list:
            if isinstance(element, list):
                #capture length of list
                length = len(element)
                print("length of list is: ", length)
                #traverse the list
                traverse_nest(element)   
            #if it not a nested list, move onto the next element of the current list
            else:
                #is the current element at the end of the current list?
                if nestlist.index(element) == length - 1:
                    print("you have reached the end of the list.  Updated list is now as follows:")
                    #increase values of most-nested list by 1
                    for i in range(length):
                        nestlist[i]= (nestlist[i] + 1)
                    print(nestlist)
                    length = 0
                #if current element is not at the end of the current list, continue through rest of the loop 
                else:    
                    continue

    
traverse_nest(list2)
print(list2)
print("List 3:")
traverse_nest(list3)
print("List 4:")
traverse_nest(list4)
print("List 5:")
traverse_nest(list5)


