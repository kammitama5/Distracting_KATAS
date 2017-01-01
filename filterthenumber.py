
def filter_string(string):
    import re
    a = re.findall(r'\d+', string)
    b = ('').join(a)
    return int(b)
	
	