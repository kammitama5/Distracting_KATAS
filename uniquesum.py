def unique_sum(lst):
      if lst == []:
        return None 
      else:
        return sum(list(set(lst)))
       