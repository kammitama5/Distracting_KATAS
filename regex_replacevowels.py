import re

def disemvowel(string):
    string = re.sub('[aeiouAEIOU]', '',string)
    print string
    
    
    
disemvowel("Hi I am Krystali")
