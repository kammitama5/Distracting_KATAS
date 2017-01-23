def bits_battle(numbers):
      arr = []
      arr1 = []
      count = 0
      count1 = 0
      for i in numbers:
        #even
        if i % 2 == 0:
          a = bin(i)
          a1 = a[2:]
          arr.append(a1)
        # odds
        elif i % 2 != 0:
          b = bin(i)
          b1 = b[2:]
          arr1.append(b1)
      x = ('').join(arr)
      y = ('').join(arr1)

      for i in x:
        if i == '0':
          count = count + 1 
      for i in y:
        if i == '1':
          count1 = count1 + 1

      if count > count1:
        return "evens win"
      elif count1 > count:
        return "odds win"
      else:
        return "tie"
		
		