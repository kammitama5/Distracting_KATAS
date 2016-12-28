import string

def greet_jedi(first, last):
  f = first[0].upper() + first[1:]
  l = last[0].upper() + last[1:] 
  fi = f[:2]
  la = l[:3]
  
  egg = "Greetings, master {}{}".format(la,fi)
  
   
greet_jedi('Beyonce', 'Knowles') # 'Greetings, master KnoBe'
greet_jedi('Chris', 'Angelico') # 'Greetings, master AngCh'
greet_jedi('grae', 'drake') # 'Greetings, master DraGr'