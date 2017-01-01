def stringy(size):
    if size == 0:
        return ''
    elif (size == 1):
        return "1"
    elif (size == 2):
        return "10"
    elif (size % 2 == 0):
        return "10" * (size / 2)
    else:
        return ("10" * ((size  - 1) / 2) + "1")
		
		