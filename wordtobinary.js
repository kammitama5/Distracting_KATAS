
function wordToBin(str){
  var arr = []
  var arr1 = []
  for (var i = 0; i < str.length; i++)
  {
    arr.push(str.charCodeAt(i));
  }
  for (var j = 0; j < arr.length; j++)
  {
    if (arr[j].toString(2).length == 8)
    arr1.push(arr[j].toString(2))
    else if  (arr[j].toString(2).length == 7)
    arr1.push('0' + arr[j].toString(2))
    else if  (arr[j].toString(2).length == 6)
    arr1.push('0' + arr[j].toString(2))
    else if  (arr[j].toString(2).length == 5)
    arr1.push('00' + arr[j].toString(2))
    else if  (arr[j].toString(2).length == 4)
    arr1.push('000' + arr[j].toString(2))
    else if  (arr[j].toString(2).length == 3)
    arr1.push('0000' + arr[j].toString(2))
    else if  (arr[j].toString(2).length == 2)
    arr1.push('00000' + arr[j].toString(2))
    else if  (arr[j].toString(2).length == 1)
    arr1.push('000000' + arr[j].toString(2))
  }
  return(arr1)
}
