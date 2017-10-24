def fillable(stock, merch, n):
    
    
    
    for key in stock:
      if merch in stock:
        if key == merch and stock[key] >= n:
          return True
          break;
        elif key == merch and stock[key] < n:
          return False
      else:
        return False
        break;
        
    return
	
	