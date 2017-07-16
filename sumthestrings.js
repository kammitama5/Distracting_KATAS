function sumStr(a,b) {
  if ((a  == null) || (b == null))
  {
    return "0"
  }
  else if ((a == "") && (b == "")){
    return "0"
  }
  else if ((a == null) || (a == "")){
    return b
  }
  else if ((b == null) || (b == "")){
    return a
  }
  else{
    return (parseInt(a) + parseInt(b)).toString();
  }
}