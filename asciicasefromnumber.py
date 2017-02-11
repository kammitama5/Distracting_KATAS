import re
def convert(number):
    arr = []
    x = re.findall('..',number)
    for i in x:
      g = (chr(int(i)))
      arr.append(g)
    return ('').join(arr)
	