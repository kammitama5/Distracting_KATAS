def lowest_temp(t):
        arr = []
        if len(t) == 0:
          return -1
        else:
          a = t.split(' ')
          for i in a:
            arr.append(int(i))
          return min(arr)
		  