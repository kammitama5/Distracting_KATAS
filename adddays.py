def nextDay(year, month, day):
    if (month == 12) and (day == 31):
        day = 1
        month = 1
        year += 1
    elif (day == 30):
        day = 1
        month += 1
    else:
        day += 1
    return(year, month, day)
