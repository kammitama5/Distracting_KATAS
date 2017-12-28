function thatUnitesUs(array1, array2, n) {
  // good luck
  var arr = []
  arr = array1.concat(array2)
  var b = arr.filter(function (item, pos){return arr.indexOf(item)== pos})
  var c = b.sort()
  return (c.slice(0,n))
}
