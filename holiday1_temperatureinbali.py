def bareable(heat, humidity):

    if (humidity > 0.5) or (heat > 35):
      return False
    elif (humidity > 0.4) and (heat > 25):
      return True
    else:
      return True
	  