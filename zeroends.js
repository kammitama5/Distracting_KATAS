function manipulate(num) { 
      var a = num.toString().length;
      var numstring = num.toString()
      var b = (a / 2) - 1 // even
      var c = parseInt(a / 2) // odd 
      if (a % 2 === 0){ // even
        return(parseInt(numstring.slice(0, c) + ("0".repeat(c))))
      }
      else { // odd
        return(parseInt(numstring.slice(0, c) + ("0".repeat(c + 1))))
        
      }
} 
