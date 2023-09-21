list1 = [[3, 7], 12, 31, 6, [1, [1, 2, 3, [87, [45, 56]]]]]
list2 = [9, 8, [2, [3, 1]], 7, [1, 12]]
list3 = []
list4 = [1, "hello", 3]
list5 = 3
length = 0


def traverse_nest(nestlist):
    length = len(nestlist)
    counter = 0
    templist = nestlist
    location = []
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
        while counter < length:
            #check if element at this index is a nested list
            print(templist[counter], "is a ", type(templist[counter]))
            #if it is a list:
            if isinstance(templist[counter], list):
                #capture length of list
                templist = templist[counter]
                length = len(templist)
                print("length of list is: ", length)
                location.append(counter)
                print("Temp list is: ", templist)
                # if counter == length:
                #     print("location list: ", location)
                # else:
                counter = 0
                    #traverse the list
                   
            #if it not a nested list, move onto the next element of the current list
            else:
                counter += 1
                if counter == length:
                    print("location list: ", location)
                    ''' 
                    ------------------------------------------------------------------------------------
                    ************************************************************************************
                    WRITE CODE HERE TO UPDATE THE VALUES OF THE NESTED LIST (IN THE ORIGINAL LIST) BY
                    ADDING 1 TO EACH VALUE.  THEN, MAKE TEMP LIST GO BACK TO ORIGINAL LIST AND CONTINUE 
                    ITERATING THROUGH TO FIND ANY OTHER NESTED LISTS. 
                    ------------------------------------------------------------------------------------
                    '''
        print(templist)
        


    
traverse_nest(list2)
print(list2)
# print("List 3:")
# traverse_nest(list3)
# print("List 4:")
# traverse_nest(list4)
# print("List 5:")
# traverse_nest(list5)


