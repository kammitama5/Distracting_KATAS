import re
def remove(s):
    a = re.sub(r'!', "", s)
    b = a + "!"
    return b
	