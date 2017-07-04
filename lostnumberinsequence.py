def find_deleted_number(arr, mixed_arr):
    total = 0
    total1 = 0
    
    for i in arr:
        total = total + i 
     
    for i in mixed_arr:
        total1 = total1 + i 
     
    diff = total - total1 
    
    return diff;
	
	