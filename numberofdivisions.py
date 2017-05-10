def divisions(n, divisor):
    total = 0;
    while (n >= divisor):
      total = total + 1 
      n = n / divisor
      
    return total
	
	