def sorter(textbooks):
    return sorted(textbooks, key=lambda v: (v.upper(), v[0].islower()))
	