function highestNumb(arr) {
  if (arr.length == 0){
    return one;
  }
  arr = arr.sort(function (a, b) {  return a - b;  });
  var a = arr.length - 1
  if ((arr.length == 0) || (arr == [])){
    return 1/0
    }
  else{
  return arr[a]
  }

}
