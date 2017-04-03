def is_lucky(n):
    a = list(str(n))
    total = 0;
    for i in a:
        total = total + int(i)
        
    if ((total == 0) or (total % 9 == 0)):
        return True
    else:
        return False
		