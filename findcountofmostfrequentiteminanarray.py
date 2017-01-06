def most_frequent_item_count(collection):
    
    if len(collection) <= 0:
      return 0 
    else:
      a = max(set(collection), key=collection.count)
      return collection.count(a)
	  
	  