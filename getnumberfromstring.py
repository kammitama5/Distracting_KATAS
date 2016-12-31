import re

def get_number_from_string(string):
  
      num = string.split(' ')
      num2 = ('').join(num)
      number = re.findall(r'\d+', num2)
      join1 = ('').join(number)
      return join1
    