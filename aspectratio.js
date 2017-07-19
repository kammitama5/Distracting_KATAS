function aspectRatio(x,y){
  var arr = []
  var x1 = 1.0/(9.0/16.0) * y * 1.0
  var y1 = y
  arr.push(Math.ceil(x1))
  arr.push(y1)
  return arr;
}

