function polygonArea(A,B,C,D){
      var rectangle = A * B
      var triangle = ((C - A) * B) / 2.0
      return (rectangle + triangle)
}
