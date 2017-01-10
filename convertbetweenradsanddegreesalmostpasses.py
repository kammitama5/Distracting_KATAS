#math already imported, default degrees and radians methods disabled

def degrees(rad):
    b = str(int((rad * (180 / math.pi))))
    return b + 'deg'
    

def radians(deg):
    a = (deg * math.pi) / 180
    if a == 0:
       b = 0
       c = str(b)
    else:
        b =  round(a, 2)
        c = str(b)
    return c + "rad"
    
math.degrees=degrees
math.radians=radians

