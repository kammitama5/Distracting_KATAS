function battle(x, y) {
    var total1 = 0;
    var total2 = 0;
    var arr = []
    var arr1 = []
    
    for (var i = 0; i < x.length; i++)
      arr.push(x[i].charCodeAt());
    for (var j = 0; j < y.length; j++)
      arr1.push(y[j].charCodeAt())
      
    for (var c = 0; c < arr.length; c++)
      total1 = total1 + arr[c]
    
    for (var d = 0; d < arr1.length; d++)
      total2 = total2 + arr1[d]
      
    if (total1 == total2){
      return "Tie!"
    }
    else if (total1 > total2){
      return x
    }
    else if (total2 > total1){
      return y
    }
    
    return
  
}