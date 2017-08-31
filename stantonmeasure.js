function stantonMeasure(arr){
  var count1 = 0
  var total = 0
  for (var i = 0; i < arr.length; i++){
    if (arr[i] == 1){
      count1 = count1 + 1
    }
  }
  for (var i = 0; i < arr.length; i++){
    if (arr[i] == count1){
      total = total + 1
    }
  }
  return total
}