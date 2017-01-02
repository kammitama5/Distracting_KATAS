def count_positives_sum_negatives(arr):
    if len(arr) < 1:
        return arr
    else: 
        blah = []
        counter1 = 0
        counter2 = 0
        for i in arr:
          if i > 0:
            counter1 += 1
          elif i < 0:
            counter2 += i
          elif arr == []:
            return blah
          else:
            counter = blah
        egg = counter1, counter2
        return list(egg)
		
		