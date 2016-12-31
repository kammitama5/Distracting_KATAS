def longest(words):
    long = ''
    
    for word in words:
      if len(word) > len(long):
        long = word 
    return len(long)
	