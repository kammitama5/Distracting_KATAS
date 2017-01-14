def flatten_me(lst):
     return sum( ([x] if not isinstance(x, list) else flatten_me(x)
		     for x in lst), [] )
 