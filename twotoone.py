def longest(s1, s2):
        a = set(s1 + s2) 
        b = sorted(a)
        g = ('').join(b)
        return g
		
		