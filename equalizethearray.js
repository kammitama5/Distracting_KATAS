function equalize(array){
      var arr = []
      if (array.length === 0){
        arr = []
      }
      else{
        var a = array[0]
        for(var i = 0; i < array.length; i++){
          var g = array[i] - a 
          if (g < 0){
            arr.push( g.toString())
          }
          else{
            arr.push("+" + g.toString())
          }
        }
      }
      return arr;
}
