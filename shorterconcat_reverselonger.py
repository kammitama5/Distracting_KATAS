def shorter_reverse_longer(a,b):
    if (len(a) > len(b)):
        return b + a[::-1] + b
    elif(len(b) > len(a)):
        return a + b[::-1] + a
    elif (len(a) == len(b)):
        return b + a[::-1] + b 
    elif ((len(a) == 0)):
        return a
    elif (len(b) == 0):
        return b
    else:
        return "hmm"
		
		