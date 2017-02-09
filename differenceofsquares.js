function differenceOfSquares(x){
      var total = 0 
      var square = 0
      
      for (var i = 0; i <= x; i++){
        total = total + i 
        square = square + Math.pow(i, 2)
      }
      
      var totalsquared = total * total 

      var result = totalsquared - square 
      return (result)
}

