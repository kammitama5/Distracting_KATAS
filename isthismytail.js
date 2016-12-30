function correctTail(bod, tail){ 
  
  var sub = bod.substr(bod.length-(tail.length))
  
  if (sub == tail){
    return true
  }
  else {
    return false
  }
}

