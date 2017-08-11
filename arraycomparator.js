function matchArrays(v,r){
  var total = 0
  for (var i = 0; i < v.length; i++){
    for (var j = 0; j < r.length; j++){
      if (v[i] == r[j]){
        total = total + 1
      }
    }
  }
  return total
}
