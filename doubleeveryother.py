def double_every_other(lst):
      listy = []
      for count, i in enumerate(lst):
          if count % 2 == 1:
            listy.append(i * 2)
          else:
            listy.append(i)
      return listy
	  
	  