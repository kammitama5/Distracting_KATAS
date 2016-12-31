import re

def string_clean(s):
    s = re.sub("\d+", "", s)
    return s
	
	