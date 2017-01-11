def enough(cap, on, wait):
    if (cap == (on + wait)):
        return True
    elif (cap < (on + wait)):
        return ((on + wait) - cap)
    elif (cap > (on + wait)):
        return True
    else:
        return False
		
		