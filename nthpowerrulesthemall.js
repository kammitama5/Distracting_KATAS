function modifiedSum(a, n) {
  var power = 0 
  var total = 0 
  for (var i = 0; i < a.length; i++){
    power = power + Math.pow(a[i], n)
    total = total + a[i]
  }
  return(power - total)
}
