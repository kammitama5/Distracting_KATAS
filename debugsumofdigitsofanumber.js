
function getSumOfDigits(integer) {
  var sum = 0
  var digits = Math.abs(integer)
  var digits1 = digits.toString()
  
  for (var i = 0; i < digits1.length; i++){
      sum += parseInt(digits1.charAt(i), 10)
      
  }
 
  return sum
}

