from random import randint
import random
def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        print(random_noun())
    elif word == "VERB":
        print(random_verb())
    else:
        print word[0]
        
word_transformer("NOUN")
