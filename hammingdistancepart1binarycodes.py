def hamming_distance(a, b):
    # Your code here
  total = 0
  for i, j in zip(a, b):
                if i != j:
                        total += 1
     
  return total
  