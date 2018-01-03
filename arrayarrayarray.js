function explode(x){
  var arr = []
  var count = 0;
  if (x[0] == parseInt(x[0])){  
      var a = x[0]
      count = count + a;
      }
  if (x[1] == parseInt(x[1])){  
      var b = x[1]
      count = count + b;
      }
  x[1]
  for (var i = 0; i < count; i++)
  {
    arr.push(x)
  }
  if (count == 0){
    return "Void!"
  }
  else{
    return arr
  }
}
