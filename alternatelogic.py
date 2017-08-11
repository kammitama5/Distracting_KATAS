def alt_or(lst):
    total = 0
    if len(lst) == 0:
        return None
    else:
        for i in lst:
            if i == False:
                total = total + 0
            elif i == True:
                total = total + 1 
    if total > 0:
        return True
    else:
        return False
		