def repeater(string, n):
  
  print('"{}" repeated {} times is: "{}"'.format(string, str(n), string * n))
  
  
  return
  


repeater('yo', 3)  # '"yo" repeated 3 times is: "yoyoyo"')
repeater('WuB', 6)  #'"WuB" repeated 6 times is: "WuBWuBWuBWuBWuBWuB"')

repeater('code, eat, code, sleep... ', 2)  # '"code, eat, code, sleep... " repeated 2 times # is: "code, eat, code, sleep... code, eat, code, sleep... "')