function noOdds( values ){
  arr = []
  arr1 = []
  for (var i = 0; i < values.length; i++){
    if (i % 2 == 0) {
      arr.push(i)
    }
    else{
      arr1.push(i)
    }
    
  }
  return arr
}

