function diffBig2(arr) {
  var a = Math.max.apply(null, arr)
  var b = arr.indexOf(a)
  arr.splice(b, 1)
  var c = Math.max.apply(null, arr)
  var diff = a - c 
  return(diff)
}
