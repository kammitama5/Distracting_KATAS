import re

def disemvowel(string):
    troll = re.sub(r'[AEIOU]','', string, flags=re.IGNORECASE)
    return troll
    