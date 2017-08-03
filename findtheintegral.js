function integrate(coefficient, exponent) {
  var b = exponent + 1.0
  var a = ((coefficient) * 1.0) / b
  return a.toString() + 'x^' + b.toString()
}

