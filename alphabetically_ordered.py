def alphabetic(s):  # s is a lowercase string
    b = sorted(s)
    c = ('').join(b)
    return c == s 
	