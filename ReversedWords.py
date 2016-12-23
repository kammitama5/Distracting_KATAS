# Reversed words
def reverseWords(str):
  wonder = str.split(" ")
  #print wonder
  for i in wonder:
    wonder1 = list(reversed(wonder))
  #print wonder1
  wonder2 = ' '.join(wonder1)
  print wonder2
  #print(type(wonder2))