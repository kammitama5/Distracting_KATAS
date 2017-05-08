def remove_rotten(bag_of_fruits):
    a = bag_of_fruits
    arr = []
    if a == None:
        return []
    else:
        for i in a:
          if i[:6] == "rotten":
            b = arr.append(i[6:].lower())
          else:
            b = arr.append(i)
        return arr
		
		