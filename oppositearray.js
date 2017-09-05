function oppositeArray(numbers) {
  var arr = []
  for (var i = 0; i < numbers.length; i++){
    arr.push(0 - numbers[i])
  }
  return arr
}
