def excludingVatPrice(price):
    if ((price == None) or (price < 0)):
        return -1 
    else:
        a = (price / 115.0) * 100.0 
        return round(a, 2)
		