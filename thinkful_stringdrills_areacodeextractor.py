import re

def area_code(text):
    w = re.findall("[(][\d]{3}[)]", text)
    #print w
    q = ''.join(w)
    return q[1:4]