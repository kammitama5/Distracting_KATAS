function addArrays(array1, array2) {
  var arrayToNumber1 = parseInt(array1.join(''));
  var arrayToNumber = parseInt(array2.join(''));
  var arr3 = arrayToNumber1 + arrayToNumber;
  var arr4 = (arr3.toString())
  arr = arr4.split("")
  var final = []
  for (var i = 0; i < arr.length; i++){
    final.push(parseInt(arr[(i)]))
  }
  return final
}
