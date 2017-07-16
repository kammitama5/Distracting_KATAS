function bigWordFinder(string){
  arr1 = []
  arr2 = []
  var a = string.split(" ");
  for (var i = 0; i < a.length; i++)
    {
      arr1.push(a[i].length)
    }
    
    var b  = arr1.sort(function (a, b) {  return a - b;  });
    var d = arr1.length - 1
    var c = b[d]
    
    for (var i = 0; i < a.length; i++)
    {
      if (a[i].length == c)
      {
        arr2.push(a[i]) 
        arr2.push(c)
      }
    }
   
    
  return arr2
  
}

