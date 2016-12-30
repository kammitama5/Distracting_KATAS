def getCount(inputStr):
    num_vowels = 0
    
    for i in inputStr:
      if i == "a" or i == "A":
        num_vowels = num_vowels + 1
      elif i == "e" or i == "E":
        num_vowels = num_vowels + 1
      elif i == "i" or i == "I":
        num_vowels = num_vowels + 1 
      elif i == "o" or i == "O":
        num_vowels = num_vowels + 1
      elif i == "u" or i == "U":
        num_vowels = num_vowels + 1
      else:
        num_vowels
        
    return num_vowels
        