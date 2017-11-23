const rotateToMax = n => {
// set to string in case tests contain strings
  var str = n.toString()
  // split and push to int array
  var strarr = str.split("")
  var arr = []
  for (var i = 0; i < strarr.length; i++){
    arr.push(parseInt(strarr[i]))
  }
  // sort ints and reverse 
  var arr = arr.sort(function(a, b){return a - b});
  var arr1 = arr.reverse();
  // join number again 
  var final = arr1.join("")
  var final1 = parseInt(final)
  
  return final1
}

rotateToMax(123)
rotateToMax(786)
