function getRectangleString(width, height) {
  var a = ("*").repeat(width) + "\n"
 
  var mid = ("*" + "\n").repeat(height-2)
  
 
  var b = ("*").repeat(width);
  console.log(a+mid+b)
}


//getRectangleString(3, 3)
getRectangleString(4, 4)

