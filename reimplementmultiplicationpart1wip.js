function mul(a, b) {
  if ((a == 0) || (b == 0)){
    return 0
  }
  else if (a == 1){
    return b
  }
  else if (b == 1){
    return a 
  }
  else{
    var n = Math.round(Math.pow(10,(Math.log10(a) + Math.log10(b))))
  }
  
  return n
}
