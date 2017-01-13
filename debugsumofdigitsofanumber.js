function getSumOfDigits(integer) {
  var sum = 0;
  var digits =  Math.abs(integer).toString();
  console.log(digits)
  for(var i = 0; i < digits.length; i++) {
    sum = sum + parseInt(digits[i]);
  }
  return sum;
}
