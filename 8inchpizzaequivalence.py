def how_many_pizzas(n):
    a = 64.0
    c = n * n
    b = (c / a)
    
    d = list(str(b))
    d1 = str(b)
    
    
    integer = int(b)
    
    length = len(d)
    finddot = d.index('.')
    
    secondpart = d1[(finddot):length]
    
    fraction = float(secondpart) * 8
    fraction1 = str(fraction)
    fractionfirst = fraction1[0]

    return 'pizzas: {}, slices: {}'.format(integer, fractionfirst)
	
	