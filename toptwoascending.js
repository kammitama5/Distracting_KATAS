function lastTwo(x){
  var y = x.sort(function(a, b){return a-b}).reverse();
  return y.slice(0,2).reverse()
}
