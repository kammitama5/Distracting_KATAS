function averageLength(array) { 
  var count = 0
  var array1 = []
  var len = array.length
  for (var i = 0; i < array.length; i++)
  {
    count = count + array[i].length
  }
  var average = parseInt(Math.round(count / len))
  for (var j = 0; j < array.length; j++){
    array1.push(array[j][0].repeat(average))
  }
 
  return array1
}
