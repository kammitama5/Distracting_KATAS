def borrow(s):
    import re
    s = re.sub(r'\W+', '', s)
    return s.lower()
	