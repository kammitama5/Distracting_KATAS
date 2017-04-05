def mine_color(line, number):
    if ((line == 'a') and (number % 2 != 0)):
        return 'black'
    elif ((line == 'b') and (number % 2 == 0)):
        return 'black'
    elif ((line == 'c') and (number % 2 != 0)):
        return 'black'
    elif ((line == 'd') and (number % 2 == 0)):
        return 'black'   
    elif ((line == 'e') and (number % 2 != 0)):
        return 'black'
    elif ((line == 'f') and (number % 2 == 0)):
        return 'black' 
    elif ((line == 'g') and (number % 2 != 0)):
        return 'black'
    elif ((line == 'h') and (number % 2 == 0)):
        return 'black' 
    else:
        return 'white'
		
		