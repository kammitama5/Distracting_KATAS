
def nextDay(year, month, day):
    
    if (month == 12) and (day == 30):
        day = 1
        month = 1
        year = year + 1
    elif (day == 30):
        day = 1
        month = month + 1
    else:
        
        day = day + 1
    return(year, month, day)

