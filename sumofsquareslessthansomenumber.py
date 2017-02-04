import math
def get_number_of_squares(n):
        arr = []
        total = 0 
        for i in range(0, n+1):
         if total < n:
           total = total + i * i
           arr.append(i)
        return arr[-2]
		