function makeParts(arr, chunkSize) {
      
      var arr1 = []
      i = 0 
      n = arr.length
      
      while (i < n){
        arr1.push(arr.slice(i, i += chunkSize))
      }
      return(arr1)
}
