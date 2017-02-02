
import math
def arithmetic_sequence_sum(a, r, n):
        count = 0
        for i in range(0, n):
          b = a + (i * r)
          count = count + b
        return count
		