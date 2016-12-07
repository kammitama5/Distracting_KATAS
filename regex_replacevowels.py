import re

def disemvowel(string):
    string = re.sub('[aeiouAEIOU]', '',string)
    print string
    
    
    
disemvowel("Hi I am Krystali")
# Actually pretty proud that this worked out! Regex ftw!
