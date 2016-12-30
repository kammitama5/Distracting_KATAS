function oddOnly(arr1){
    
    arr2 = []
    
    for (var i = 0; i < arr1.length; i++){
      if (arr1[i] % 2 != 0){
        arr2.push(arr1[i])
      }
      
    }
    return(arr2)
  
}
