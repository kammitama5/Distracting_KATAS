function reverseByCenter(s){
    // even number of letters
    if (s.length % 2 != 0){
      a1 = parseInt((s.length / 2))
      var r1 = s[a1]
      var q1 = s.slice(0, (0, a1 ))
      var c1 = s.slice(1+a1 )

      return(c1 + r1 + q1)
      
      
      
    }
    // odd number letters
    else {
      a = s.length / 2
      w = parseInt(a)
      var q = s.slice(0, w)
      var c = s.slice(w)
      return(c + q)
    
      
      
       
      
      
    }
    
  

  
}

