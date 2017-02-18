def validate_sequence(sequence):
      a= len(sequence)
      arr = []
      diff = sequence[1] - sequence[0]
      for i in range(sequence[0], sequence[-1]+1, diff):
        arr.append(i) 
      
      if sequence == arr:
        return True
      else:
        return False
		