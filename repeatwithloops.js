function hasOneChar(s) {
      var total = 0;
      var le = s.length;
      var first = s[0]
      var ascii = s.charCodeAt(0)
      var multasc = ascii * le 
      //var div = multasc  / le
      
      for (var i = 0; i < s.length; i++){
        total = total + s.charCodeAt(i)
      }
      var mult = total / multasc
      if (parseInt(mult) === mult){
        return(true)
      }
      else{
        return(false)
      }
}
