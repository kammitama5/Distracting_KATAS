def factorial(n):
    total = 1
    if n < 0:
        return None
    if n == 0:
        return 1 
    else:
        for i in range(2, n+1):
            total = total * i
        return total
		
		