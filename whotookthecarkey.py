def who_took_the_car_key(message):
    arr = []
    for i in message:
      arr.append((chr(int(i, 2))))
    w = ''.join(arr)
    return w
	
	