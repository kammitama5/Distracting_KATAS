def dont_give_me_five(start,end):
    count = 0
    for i in range(start, (end + 1)):
      g = str(i)
      if not '5' in g:
        count = count + 1
    return count
	