function isInArray(value, array) {
  var arr = []
  for (var i = 0; i < array.length; i++)
  {
    if (array[i] == value){
      arr.push(true)
    }
  }
  if (arr.length > 0){
    return(true)
  }
  
    else{
      return(false)
    }
}
