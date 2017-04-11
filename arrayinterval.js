function arrayInterval(array, start, end) {
  var arr = []
  for (var i = 0; i < array.length; i++){
    if ((array[i] >= start) && (array[i] <= end)){
      arr.push(array[i])
    }
  }
  return arr
}