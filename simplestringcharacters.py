def solve(s):
    ## Upper, Lower, digits, special chars 
    ## overall count 
    ## uppercase count 
    ## lowercase count
    ## rest is special chars 
    
    ## first get len of s 
    s_length = len(s)
    common = "abcdefghijklmnopqrstuvwxyz"
    common_list = list(common)
    capital = common.upper()
    capital_list = list(capital)
    numbers = "0123456789"
    numbers_list = list(numbers)
    capital_count = 0
    common_count = 0
    number_count = 0
  
    #define arr to store output
    arr = []
    
    # this var gets the count of all letters counted so far 
    count = 0
    
    # make a list of s to get each char separately
    s_list = list(s)
    #print s_list 
    
    ## loop through and check to see if each condition is satisfied
    for i in s_list:
      if i in capital:
        count = count + 1
        capital_count = capital_count + 1
      elif i in common:
        count = count + 1 
        common_count = common_count + 1
      elif i in numbers:
        count = count + 1
        number_count = number_count + 1
      
    special_chars = len(s) - count 
      
    ## make an array to echo output format
    ## uppercase, lowercase, digits, special_chars
    arr.append(capital_count)
    arr.append(common_count)  
    arr.append(number_count)
    arr.append(special_chars)

    return arr
