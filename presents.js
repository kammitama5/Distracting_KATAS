function presents(a){
  var arr = []
  var len = a.length
  for (var i = 0; i < a.length; i++)
  {
    arr.push(a.indexOf(i+1)+1)
  }
  return arr
}
