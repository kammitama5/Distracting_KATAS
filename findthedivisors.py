def divisors(integer):
        n = integer
        arr = []
        for i in range(2, n):
          if n % i == 0:
            a =  i
            arr.append(a)
        if len(arr) == 0:
          return "{} is prime".format(n)
        else:
          return arr
		  