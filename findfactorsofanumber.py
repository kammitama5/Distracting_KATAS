def factors(x):
      if (type(x) != int):
        return -1 
      elif (x <= 0):
        return -1 
      else:
        y = [a for a in range(1, x+1) if x % a == 0]
        return y[::-1]
        