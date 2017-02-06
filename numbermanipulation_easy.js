function manipulate(num) { 

      var a = num.toString()
      var b = parseInt(a.length / 2.0)
      var c =(a.slice(0, b))
      var d = c + ('0'.repeat(a.length - b))
      return (parseInt(d))

} 
