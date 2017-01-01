function squareArea(A){
      console.log(A)
      side = (4.0 * A) / (2.0 * Math.PI)
      a = (side * side)
      
      return Math.round(a * 100) / 100 
}