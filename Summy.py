def summy(String):
    try:
        total = 0
        for i in String:
            total = total + int(i)
        return total
    except:
        total = 0
        a = String.split(' ')
        for i in a:
            total = total + int(i) 
        return total
		