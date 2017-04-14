function foldTo(distance) {
      var c = 1;
      var t = .0001;
      var a = distance / t
      console.log(a)
      if (distance <= 0){
        return null
      }
      else{
      for (var i = 1; i < a; i++){
        if (Math.pow(2, i) > a){
          var a = i;
          return(i)
          break;
          
        }
      }
    }
     return parseInt(a) 
       
}

foldTo(384000000)//,42