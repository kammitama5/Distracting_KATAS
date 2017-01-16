def nba_extrap(ppg, mpg):
    if (ppg == 0) or (mpg == 0):
      print 0 
    else:
      a = ((ppg * 10.0 / mpg * 10.0) / 100.0) * 48
      return round(a, 1)
	  