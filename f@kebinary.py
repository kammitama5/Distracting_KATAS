import operator

def fake_bin(x):
  list1 = []
  for char in x:
    if ((char == '0') | (char == '1') | (char == '2') | (char == '3') |
    (char == '4')):
      list1.append(0) 
    else:
      list1.append(1) 
  
  list3 = ''.join(map(str, list1))
  
  
  return list3
  

fake_bin('45385593107843568')
fake_bin('509321967506747')
fake_bin('366058562030849490134388085')

