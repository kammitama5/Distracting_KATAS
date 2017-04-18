def factors(integer, limit):
      arr = []
      if limit > integer:
        return []
      else:
        for i in range(limit, integer+1):
          if integer % i == 0:
            arr.append(i)
        return arr
		