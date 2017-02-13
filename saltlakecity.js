function fSquared (arr) {
    var square = 0
    var count = 0
    var arr1 = []
    if (!arr.some(isNaN)){
    for (var i = 0; i < arr.length; i++){
      var square = arr[i] * arr[i]
      if (square % 2 == 0){
        count = count + square
      
      }
    }
    }

    else{
      count = (undefined)
    }
    return(count)
    
};


