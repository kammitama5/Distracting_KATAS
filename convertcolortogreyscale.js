var color2grey = function (image) {
      var total = 0;
      var total1 = 0;
      var total2 = 0;
      var total3 = 0;
      
      var a1 = []
      var b1 = []
      var c1 = []
      var d1 = []
      
      var a = image[0][0]
      var b = image[0][1]
      var c = image[1][0]
      var d = image[1][1]
      //a
      for (var i =0 ; i < a.length; i++)
      {
        total = total + a[i]
      }
      avg1 = total / 3
      a1.push(avg1)
      for (var i = 1; i < a.length; i++)
      {
        a1.push(avg1)
      }
      //b
      for (var i =0 ; i < b.length; i++)
      {
        total1 = total1 + b[i]
      }
      avg2 = parseInt(total1 / 3)
      b1.push(avg2)
      for (var i = 1; i < b.length; i++)
      {
        b1.push(parseInt(avg2))
      }
      //c 
      for (var i =0 ; i < c.length; i++)
      {
        total2 = total2 + c[i]
      }
      avg3 = parseInt(total2 / 3)
      c1.push(avg3)
      for (var i = 1; i < c.length; i++)
      {
        c1.push(parseInt(avg3))
      }
      //d
      for (var i =0 ; i < d.length; i++)
      {
        total3 = total3 + d[i]
      }
      avg4 = parseInt(total3 / 3)
      d1.push(avg4)
      for (var i = 1; i < d.length; i++)
      {
        d1.push(parseInt(avg4))
      }
      first = []
      second = []
      super1 = []
      
      first.push(a1)
      first.push(b1)
      second.push(c1)
      second.push(d1)
      super1.push(first)
      super1.push(second)
      
      return(super1)
      
}