def paul(x):
    count = 0
    for i in x:
      if i == 'kata':
          count = count + 5 
      elif i == 'Petes kata':
          count = count + 10 
      elif i == 'life':
          count = count + 0 
      elif i == 'eating':
          count = count + 1
          
    if count < 40: 
        return 'Super happy!'
    elif ((count >= 40) and (count < 70)):
        return 'Happy!'
    elif ((count >= 70) and (count < 100)):
        return 'Sad!'
    elif count >= 100:
        return 'Miserable!'
    else:
        return "whoops"
		