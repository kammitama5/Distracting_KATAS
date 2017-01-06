function getDecimal(n){
  b = []
  n1 = Math.abs(n)
  a = n1.toString()
  for (var i = 1; i < a.length; i++){
      b.push(a[i])
  }
  c = b.join("")
  d = Number(c)
  return d
  
  
  
}


getDecimal(2.4)  == 0.4
getDecimal(-0.2) == 0.2
