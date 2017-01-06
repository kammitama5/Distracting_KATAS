def remove_every_other(my_list):
    listy = []
    for count, i in enumerate(my_list):
          if (count % 2 == 0):
            listy.append(i)
          
    return listy
	
	