function differenceInAges(ages){
  var arr = []
  var ages1 = ages.sort((a, b) => a - b);
  var minim = ages1[0]
  var maxim = ages1[ages1.length - 1]
  var diff = maxim - minim

  arr.push(minim)
  arr.push(maxim)
  arr.push(diff)
  
  return arr
}

