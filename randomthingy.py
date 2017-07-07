import random
def random_noun():
    number = random.randint(0,1)
    if number == 0:
      return "run"
    else:
      return "kayak"
    
    
print(random_noun())
