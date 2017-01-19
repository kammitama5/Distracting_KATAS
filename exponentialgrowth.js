function exp(n) {
  arr = []
  if (n > 0){
    for (var i = 0; i <= n; i++){
      a = Math.pow(2, i)
      arr.push(a)
    }
    }
  else if (n == 0){
    arr.push(1)
  }
  else{
    for (var i = 0; i <= Math.abs(n); i++){
      a = 0 - (Math.pow(2, i))
      arr.push(a)
    }
    
  }
    return arr
    
}
