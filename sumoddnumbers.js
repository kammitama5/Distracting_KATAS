function cubeOdd(arr) {
  arr1 = []
  sum1 = 0
  undef = undefined
  for (var i = 0; i < arr.length; i++){
    if (arr[i] != parseInt(arr[i])){
      arr1.push(undefined)
    }
    else{
      if (arr[i] % 2 != 0){
        arr1.push(Math.pow(arr[i], 3))
      }
    }
    
  }
wonderbread = arr1.includes(undef)
if (wonderbread == true){
  sum1 = undefined
}
else{
  sum1 = arr1.reduce(function (arr1, b){ return arr1 + b;}, 0)
}
return sum1

}
