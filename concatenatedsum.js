function checkConcatenatedSum(number, n){
  var arr = []
  var num = Math.abs(number)
  var num1 = num.toString()
  var num2 = (num1.split(""))
  var total = 0
  
  for (var i = 0; i < num2.length; i++){
    arr.push(num2[i].repeat(n))
  }
  //console.log(arr)
  for (var j = 0; j < arr.length; j++){
    total = total + parseInt(arr[j])
  }
  //console.log(total)
  
  if (total == num){
    return true
  }
  else{
    return false
  }
}