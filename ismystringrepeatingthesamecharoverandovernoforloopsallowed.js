function hasOneChar(s) {
      if (s.length == 1){
        return true;
      }
      else{
        var first = s[0]
        var len = s.length
        var fullstring = first.repeat(len)
        if (fullstring === s){
          return true
        }
        else{
          return false
        }
      }
      return
}

