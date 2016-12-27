def get_mixed_num(fraction):
    frac = fraction.split('/')
    #print frac
    arr = []
    w = int(frac[0])
    q = int(frac[1])
    whole = w / q
    num = w % q
    denom = q
    ans = str(whole) + " " + str(num) + "/" + str(denom)
    print ans
      
    return
  
  
get_mixed_num('18/11') # '1 7/11'
get_mixed_num('13/5') # '2 3/5'
get_mixed_num('75/10') # '7, 5/10'