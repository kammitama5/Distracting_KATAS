var sumR = function(x) {
  return (x.length === 0) ? 0 : x[0] + sumR(x.slice(1))
}
