function derive(coefficient,exponent) {
  var a = coefficient * exponent
  var b = exponent - 1
  return a.toString() + "x^" + b.toString();
}

