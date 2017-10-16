function theLongest(text){
  var a = text.split(" ")
  var arr = []
  longestword = ""
  for (var i = 0; i < a.length; i++)
    {
      arr.push(a[i].length)
    }
  var biggest = Math.max.apply(null, arr)
  for (var i = 0; i < a.length; i++){
    if (a[i].length == biggest){
      longestword = a[i]
    }
  }
  return longestword
}
