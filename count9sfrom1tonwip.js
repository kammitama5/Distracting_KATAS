function number9(n){
  count = 0
  arr = []
  for (var i = 1; i <= n; i++){
    var a = i.toString()
    arr.push(a)
  }
  var b = arr.join('')
  for (var j = 0; j < b.length+1; j++){
    if (b[j] == '9'){
      count = count + 1
    }
  }
  return(count)
}
