function evenChars(string){
      arr = []
      if ((string.length <= 1) || (string.length > 100)){
          return "invalid string"
      }
      else{
      for (var i = 1; i <= string.length - 1; i+=2){
            b = (string[i])
            arr.push(b)
            
      }
      return arr
      }
}
