def number(bus_stops):
    counter1 = 0
    counter2 = 0
    for i in bus_stops:
      counter1 = counter1 + i[0]
      counter2 = counter2 + i[1]
      
    w = abs(counter2 - counter1)
    return w
	
	
      