def fizzbuzz(n):
    if (n % 3) == 0 and (n % 5) == 0:
        return "fizz buzz"
    elif (n % 5) == 0:
        return "buzz"
    elif (n % 3) == 0:
        return "fizz"
    else:
        return n
    
    
