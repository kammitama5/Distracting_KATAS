def calculate_age(year_of_birth, current_year):
  
        diff = current_year - year_of_birth
        
        # for 0, for -1, for -ves, for 1, for +ves
        if diff == 0:
          return "You were born this very year!"
        elif diff == -1:
          return "You will be born in 1 year."
        elif diff == 1:
          return "You are 1 year old."
        elif (diff < 0) and (not(diff == -1)):
          return "You will be born in {} years.".format(abs(diff))
        else:
          return "You are {} years old.".format(diff)
		  
		  