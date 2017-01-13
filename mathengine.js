function mathEngine(arr) {
      
      var count1 = 0 
      var count = 1
      if (arr == null){
        return 0
      }
      else if (arr.length == 0){
        return 1
      }
      else{
        for (var i = 0; i < arr.length; i++){
        if (arr[i] >= 0){
          count = count * arr[i]
        }
        else{
          count1 = count1 + arr[i]
        }
      }
      a = count + count1
     
      return a
      }
      
}
