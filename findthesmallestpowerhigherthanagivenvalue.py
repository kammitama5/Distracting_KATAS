import math
def find_next_power(val, pow_):
    x = int(math.pow(val, (1.0/pow_)))
    y = x + 1
    z = math.pow(y, pow_)
    return int(z)
	