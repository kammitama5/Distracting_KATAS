let strOfNums = (num1, num2) => {
  if (num1 < num2){
    var min1 = num1
    var max1 = num2
  }
  else{
    var min1 = num2
    var max1 = num1
  }
  var string1 = ""
  for (var i = min1+1; i < max1; i++)
    {
      string1 = string1 + i.toString()
    }  
    return string1
}

