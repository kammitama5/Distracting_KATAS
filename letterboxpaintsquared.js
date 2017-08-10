var paintLetterboxes = function(start, end) {
  var arr1 = []
  var arr = []
  var a1 = 0
  var b1 = 0
  var c1 = 0
  var d1 = 0
  var e1 = 0 
  var f1 = 0
  var g1 = 0
  var h1 = 0 
  var j1 = 0 
  var k1 = 0
  
  for (var i = start; i <= end; i++)
  {
    arr.push(i.toString())
  }
  var a = arr.join("")
  var b = a.split("")
  console.log(b)
  for (var i = 0; i < b.length; i++)
  {
    if (b[i] == "0"){
      a1 = a1 + 1
      
    }
    else if (b[i] == "1"){
      b1 = b1 + 1
      
    }
    else if (b[i] == "2"){
      c1 = c1 + 1
     
    }
    else if (b[i] == '3'){
      d1 = d1 + 1
      
    }
    else if (b[i] == '4'){
      e1 = e1 + 1
     
    }
    else if (b[i] == '5'){
      f1 = f1 + 1
     
    }
    else if (b[i] == '6'){
      g1 = g1 + 1
      
    }
    else if (b[i] == '7'){
      h1 = h1 + 1
     
    }
    else if (b[i] == '8')
    {
      j1 = j1 + 1
      
    }
    else if (b[i] == '9'){
      k1 = k1 + 1
      
    }
  }
  arr1.push(a1)
  arr1.push(b1)
  arr1.push(c1)
  arr1.push(d1)
  arr1.push(e1)
  arr1.push(f1)
  arr1.push(g1)
  arr1.push(h1)
  arr1.push(j1)
  arr1.push(k1)
  
  return arr1
}
