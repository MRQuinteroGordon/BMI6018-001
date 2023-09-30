def exception_add_function(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [4,5,6]
   
   If the lists are lists of strings, concatenate them
   Example:
      > wrong_add_function(['1','2','3'],['1','1','1'])
      > ['1111','2111','3111']
   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.
   # add 2.b here
   # add 2.c function here
   '''
   try:
      print("arg1 is: ", arg1, "and the sum is: ", sum([type(i)==str for i in arg1]))
      print("arg2 is: ", arg2, "and the sum is: ", sum([type(i)==str for i in arg2]))
      #numeric section
      if sum([type(i)==int for i in arg1])==len(arg1) and \
         sum([type(i)==int for i in arg2])==len(arg2):
            arg1_index=0
            while arg1_index < len(arg1):
               arg_2_sum = 0
               for arg2_elements in arg2:
                  arg_2_sum = arg1[arg1_index] + arg2_elements
                  arg1[arg1_index]=arg_2_sum  
               arg1_index+=1
            return arg1
            # return "yayee!"
      #string section
      elif sum([type(i)==str for i in arg1])==len(arg1) and sum([type(i)==str for i in arg2])==len(arg2):
         print("arg1 is: ", arg1, "and the sum is: ", sum([type(i)==str for i in arg1]))
         print("arg2 is: ", arg2, "and the sum is: ", sum([type(i)==str for i in arg2]))
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1
         # return "yeehaw!"
      else:
         print("whoops")
         raise ValueError
   except ValueError:
      print("whoopsy doopsy")
      input_index = []
      index = 0
      for arg in range(1,3):
         arglist = []
         if arg == 1:
            arglist = arg1
         else:
            arglist = arg2
         for element in arglist:
            if type(element) != str:
               input_index.append(index)
            index += 1
         if len(input_index) > 0:
            print(f"Your input argument #{arg}, at element(s) {input_index}, are not of the expected type.  Please change this and rerun.")
         input_index = []
         index = 0
      
            

# arg_str_1=['1','2','3']
# arg_str_2=['1','1',1]
# exception_add_function(arg_str_1,arg_str_2)
# exception_add_function([1,2,3], [1,1,1])

def wrong_add_function(arg1,arg2):
   try:
      #numeric section
      if sum([type(i)==int for i in arg1])==len(arg1) and \
         sum([type(i)==int for i in arg2])==len(arg2):
            arg1_index=0
            while arg1_index < len(arg1):
               arg_2_sum = 0
               for arg2_elements in arg2:
                  arg_2_sum = arg1[arg1_index] + arg2_elements
                  arg1[arg1_index]=arg_2_sum  
               arg1_index+=1
            return arg1
      #string section
      elif sum([type(i)==str for i in arg1])==len(arg1) and sum([type(i)==str for i in arg2])==len(arg2):
         pass
      else:
         raise ValueError 
      arg1_index=0
      while arg1_index < len(arg1):
         arg_2_sum = ''
         for arg2_elements in arg2:
            arg_2_sum += arg2_elements
         arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
         arg1_index+=1
      return arg1

   except ValueError:
      correction_add_function(arg1, arg2)
 
 
def correction_add_function(list1, list2):
   index = 0
   for arg in range(1,3):
      arglist = []
      if arg == 1:
         arglist = list1
      else:
         arglist = list2
      for element in arglist:
         if type(element) != str:
            element = str(element)
         index += 1
      index = 0
   return list1, list2
#YOU LEFT OFF HERE, NEEDING TO RETURN THE VALUES TO THE ORIGINAL FUNCTION SO IT CAN PROCESS THE TWO LISTS WITHOUT SETTING OFF AN INFINITE RECURSIVE FUNCTION. YOU'RE ALSO WAITING FOR CLARIFICATION FROM THE TA'S ABOUT WHERE THE FIXING OF ARG1 AND ARG2 SHOULD BE HAPPENING. 
         
            

arg_str_1=['1','2','3']
arg_str_2=['1','1',1]

wrong_add_function(arg_str_1,arg_str_2)
wrong_add_function([1,2,3], [1,1,1])