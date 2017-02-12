#fix the function below!
import re
def convert_num(number, base):
  try:
        if base == 'hex':
            a = hex(number)
            return str(a)
        elif base == 'bin':
            a = bin(number)
            return str(a)
        elif (not(base == 'hex')) or (not(base == 'bin')):
            return "Invalid base input"
  except:
        return "Invalid number input"
		