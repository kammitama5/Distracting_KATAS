def lostSheep(friday,saturday,total):
    total1 = 0 
    total2 = 0
    for i in friday:
      total1 = total1 + i 
    for j in saturday:
      total2 = total2 + j 
    
    t = total1 + total2
    t1 = total - t 
    
    return t1
	