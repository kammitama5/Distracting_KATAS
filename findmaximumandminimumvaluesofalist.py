def min(arr):
     #print arr
     for i in range (1, len(arr)):
       if arr[i] < arr[0]:
         arr[0] = arr[i]
     return arr[0]
      
     
    

def max(arr):
    #print arr
    
    for i in range (1, len(arr)):
       if arr[i] > arr[0]:
         arr[0] = arr[i]
    return arr[0]


