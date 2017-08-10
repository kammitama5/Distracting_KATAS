function first(arr, n) {
  var arr1 = []
  if (n == null){
    arr1.push(arr[0])
  }
  else if (n == 0){
    arr1 = []
  }
  else{
    if (n > arr.length){
      return arr
    }
    else{
    for (var i = 0; i < n; i++){
      arr1.push(arr[i])
    }
    }
  }
  return(arr1)
}
