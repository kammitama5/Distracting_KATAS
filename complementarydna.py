def DNA_strand(dna):
    a = list(dna)
    arr = []

    for i in a:
      if i == 'A':
        g = i.replace('A', 'T')
        arr.append(g)
      elif i == 'T':
        g = i.replace('T', 'A')
        arr.append(g)
      elif i == 'G':
        g = i.replace('G', 'C')
        arr.append(g)
      elif i == 'C':
        g= i.replace('C', 'G')
        arr.append(g)
    
    w = ('').join(arr)
    return w
	