function rectangle(char, width, height)
{
  var arr = []
  var x = (char.repeat(width))
  //console.log(x)
  for (var i = 0; i < height; i++){
    var z = (x)
    arr.push(z)
  }
 
  return arr.join("\n")
}

