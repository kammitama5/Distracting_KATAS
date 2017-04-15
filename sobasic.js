function convertBase20ToDecimal(init){
  
  a = parseInt(init, 20)
  b = a.toString(10)
  c = parseInt(b)
  if (c == parseInt(c)){
    return parseInt(c)
  }
  else{
    return -1
  }
}
