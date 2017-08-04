function spongeMeme(sentence) {
  var arr = []
  
  for (var i = 0; i < sentence.length; i++)
  {
    if (i % 2 == 0)
    {
      arr.push(sentence[i].toUpperCase())
      
    }
    else{
      arr.push(sentence[i].toLowerCase())
    }
    
  }
  var pete = arr.join('')
  return(pete)
  return
    
}

