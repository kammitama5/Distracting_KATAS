function armstrong(num){
  var a = num.toString()
  var b = a.split("")
  var total = 0
  for (var i = 0; i < b.length; i++)
  {
    var c = Math.pow(parseInt(b[i]), 3)
    total = total + c
  }
  if (total == num){
    return(true)
  }
  else{
    return(false)
  }
  return
}
