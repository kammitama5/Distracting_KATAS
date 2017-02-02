import re 
def to_leet_speak(str):
      a = str 
      a = re.sub('[A]','@',a)
      a = re.sub('[B]','8',a)
      a = re.sub('[C]','(',a)
      a = re.sub('[E]','3',a)
      a = re.sub('[G]','6',a)
      a = re.sub('[H]','#',a)
      a = re.sub('[I]','!',a)
      a = re.sub('[L]','1',a)
      a = re.sub('[O]','0',a)
      a = re.sub('[S]','$',a)
      a = re.sub('[T]','7',a)
      a = re.sub('[Z]','2',a)
      
      return a
	  
	  